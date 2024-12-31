from django.db import models
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import path
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML

# Model for Task Management (Adrien)
class Task(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    priority = models.IntegerField(default=1)
    due_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title


# Model for Stock Management (Adrien)
class StockItem(models.Model):
    name = models.CharField(max_length=255)
    barcode = models.CharField(max_length=128, unique=True)
    quantity = models.PositiveIntegerField(default=0)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.quantity} units)"


# Model for Certificate Generation (Adrien)
class Certificate(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='certificates')
    generated_date = models.DateTimeField(auto_now_add=True)
    pdf_file = models.FileField(upload_to='certificates/')

    def __str__(self):
        return f"Certificate for {self.task.title} generated on {self.generated_date}"


# Signals for Auto-Generating Certificates (if needed)
from django.db.models.signals import post_save
from django.dispatch import receiver

def generate_certificate_pdf(task):
    html_string = render_to_string('certificate_template.html', {'task': task})
    html = HTML(string=html_string)
    pdf_file_path = f"certificates/certificate_{task.id}.pdf"
    html.write_pdf(pdf_file_path)
    return pdf_file_path

@receiver(post_save, sender=Task)
def auto_generate_certificate(sender, instance, created, **kwargs):
    if created and instance.status == 'completed':
        pdf_path = generate_certificate_pdf(instance)
        Certificate.objects.create(task=instance, pdf_file=pdf_path)

# Views for Task Management
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})

def task_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        priority = request.POST.get('priority')
        due_date = request.POST.get('due_date')
        Task.objects.create(title=title, description=description, priority=priority, due_date=due_date)
        return redirect('task_list')
    return render(request, 'task_form.html')

def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.priority = request.POST.get('priority')
        task.due_date = request.POST.get('due_date')
        task.status = request.POST.get('status')
        task.save()
        return redirect('task_list')
    return render(request, 'task_form.html', {'task': task})

# Views for Stock Management
def stock_list(request):
    stocks = StockItem.objects.all()
    return render(request, 'stock_list.html', {'stocks': stocks})

def stock_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        barcode = request.POST.get('barcode')
        quantity = request.POST.get('quantity')
        description = request.POST.get('description')
        StockItem.objects.create(name=name, barcode=barcode, quantity=quantity, description=description)
        return redirect('stock_list')
    return render(request, 'stock_form.html')

# URL Configuration
urlpatterns = [
    path('tasks/', task_list, name='task_list'),
    path('tasks/create/', task_create, name='task_create'),
    path('tasks/<int:pk>/update/', task_update, name='task_update'),
    path('stocks/', stock_list, name='stock_list'),
    path('stocks/create/', stock_create, name='stock_create'),
]
