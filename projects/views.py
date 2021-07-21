from django.shortcuts import render, redirect
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
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects-home')
    context = {'form': form}
    return render(request=request, template_name='projects/project-form.html', context=context)


def updateProject(request, pk):
    project_data = Project.objects.get(id=pk)
    form = ProjectForm(instance=project_data)

    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project_data)
        if form.is_valid():
            form.save()
            return redirect('projects-home')

    context = {'form': form}
    return render(request, template_name='projects/project-form.html', context=context)


def deleteProject(request, pk):
    project_obj = Project.objects.get(id=pk)
    if request.method == 'POST':
        project_obj.delete()
        return redirect('projects-home')
    context = {'object': project_obj}
    return render(request, template_name='projects/delete.html', context=context)



