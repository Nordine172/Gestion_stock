from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from .models import Tache

User = get_user_model()

class TacheForm(forms.ModelForm):
    class Meta:
        model = Tache
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        groupes = Group.objects.filter(name__in=['Techniciens', 'Commerciaux'])
        utilisateurs = User.objects.filter(groups__in=groupes).distinct()
        self.fields['utilisateur_assigne'].queryset = utilisateurs
