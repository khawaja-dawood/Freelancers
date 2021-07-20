from django.shortcuts import render
from django.http import HttpResponse
from .models import Project, Tag, Review
from .forms import ProjectForm


def projects(request):
    project_obj = Project.objects.all()
    context = {'projects': project_obj}
    return render(request=request, template_name='projects/projects.html', context=context)


def project(request, pk):
    project_obj = Project.objects.get(id=pk)
    # tags = project_obj.tags.all()             # for querying ManyToMany relationship
    # reviews = project_obj.reviews.all()       # reviews.all() can be used if related name is set in models
    # reviews = project_obj.review_set.all()    # ModelName_set.all() --> for querying all children of this obj
    context = {'project': project_obj}
    return render(request=request, template_name='projects/single-project.html', context=context)


def createProject(request):
    form = ProjectForm()
    context = {'form': form}
    return render(request=request, template_name='projects/project-form.html', context=context)