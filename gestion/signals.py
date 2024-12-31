from django.db.models.signals import post_save, post_migrate
from django.dispatch import receiver
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from .models import Profile

User = get_user_model()

@receiver(post_migrate)
def create_default_users_and_groups(sender, **kwargs):
    """
    Recrée les groupes et utilisateurs essentiels après une migration.
    """
    # Créer les groupes nécessaires
    groupes = ['Administrateurs', 'Techniciens', 'Commerciaux']
    for group_name in groupes:
        Group.objects.get_or_create(name=group_name)

    # Créer ou mettre à jour moi "roor"
    admin_group = Group.objects.get(name='Administrateurs')
    root, created = User.objects.get_or_create(username='root', email='hajaouan@gmail.com')
    if created:
        root.set_password('465925')
    root.is_superuser = True
    root.is_staff = True
    root.groups.add(admin_group)
    root.save()
    
    # Créer ou mettre à jour l'utilisateur "Fouzia"
    admin_group = Group.objects.get(name='Administrateurs')
    fouzia, created = User.objects.get_or_create(username='Fouzia', email='fouzia@example.com')
    if created:
        fouzia.set_password('Lilouche13')
    fouzia.is_superuser = True
    fouzia.is_staff = True
    fouzia.groups.add(admin_group)
    fouzia.save()

    # Créer ou mettre à jour l'utilisateur "Adrien"
    tech_group = Group.objects.get(name='Techniciens')
    adrien, created = User.objects.get_or_create(username='Adrien', email='adrien@example.com')
    if created:
        adrien.set_password('Lilouche13')
    adrien.groups.add(tech_group)
    adrien.save()

    # Créer ou mettre à jour l'utilisateur "Valérie"
    commercial_group = Group.objects.get(name='Commerciaux')
    valerie, created = User.objects.get_or_create(username='Valérie', email='valerie@example.com')
    if created:
        valerie.set_password('Lilouche13')
    valerie.groups.add(commercial_group)
    valerie.save()

    print("Groupes et utilisateurs essentiels créés ou mis à jour.")

#@receiver(post_save, sender=User)
#def assign_default_group(sender, instance, created, **kwargs):
#    if created:
#        if instance.groups.count() == 0:  # Si aucun groupe n'est attribué
#            techniciens_group, _ = Group.objects.get_or_create(name='Techniciens')
#            instance.groups.add(techniciens_group)

@receiver(post_migrate)
def create_groups(sender, **kwargs):
    admin_group, _ = Group.objects.get_or_create(name="Administrateurs")
    tech_group, _ = Group.objects.get_or_create(name="Techniciens")
    sales_group, _ = Group.objects.get_or_create(name="Commerciaux")

    # Vérifier que les ContentTypes nécessaires sont disponibles
    try:
        tache_content_type = ContentType.objects.get(app_label="gestion", model="tache")
        stock_content_type = ContentType.objects.get(app_label="gestion", model="stock")

        # Associer les permissions spécifiques aux groupes
        tache_permissions = Permission.objects.filter(content_type=tache_content_type)
        stock_permissions = Permission.objects.filter(content_type=stock_content_type)

        tech_group.permissions.set(tache_permissions | stock_permissions)
        admin_group.permissions.set(Permission.objects.all())
    except ContentType.DoesNotExist:
        # Si les ContentTypes ne sont pas encore créés, ignorer
        pass

# Créer un Profile dès qu'un User est créé
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:  # Si un nouvel utilisateur est créé
        Profile.objects.create(user=instance)

# Sauvegarder le Profile associé lorsqu'un User est sauvegardé
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if hasattr(instance, "profile"):
        instance.profile.save()
