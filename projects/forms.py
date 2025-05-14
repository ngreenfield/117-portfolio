from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description', 'year', 'skill', 'image', 'url']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'image': forms.ClearableFileInput(),
            'year': forms.NumberInput()
        }

    def __str__(self):
        return f"{self.cleaned_data.get('name', '')} - ({self.cleaned_data.get('year', '')})"

