from django.shortcuts import render, redirect
from .models import Project, Experience
from .forms import ProjectForm

# Create your views here.
def projects_list_view(request):

    projects = Project.objects.all().order_by('-year')

    return render(request, "projects/list.html", {"projects": projects})

def experience_view(request):

    experiences = Experience.objects.prefetch_related('skill').all()  

    return render(request, "projects/experience.html", {"experiences": experiences})  

def new_project_view(request):
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects_list')  
    else:
        form = ProjectForm()

    return render(request, "projects/new_project.html", {"form": form})

