from django.db.models import Q
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import ProjectForm
from users.models import Profile


def projects(request):
    project_obj = Project.objects.filter(active=True)
    context = {'projects': project_obj}
    return render(request=request, template_name='projects/projects.html', context=context)


def project(request, pk):
    project_obj = Project.objects.get(id=pk)
    context = {'project': project_obj}
    # tags = project_obj.tags.all()             # for querying ManyToMany relationship
    # reviews = project_obj.reviews.all()       # reviews.all() can be used if related name is set in models
    # reviews = project_obj.review_set.all()    # ModelName_set.all() --> for querying all children of this obj
    return render(request=request, template_name='projects/single-project.html', context=context)


# login_required
def create_project(request):
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.developer = request.user
            print(request.user)
            # print(Developer.objects.get())
            form.save()
            return redirect('projects-home')
    context = {'form': form}
    return render(request=request, template_name='projects/project-form.html', context=context)


def update_project(request, pk):
    project_data = Project.objects.get(id=pk)
    form = ProjectForm(instance=project_data)

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project_data)
        project_data.title = project_data.title + " (UPDATED)"
        if form.is_valid():
            form.save()
            return redirect('projects-home')

    context = {'form': form}
    return render(request, template_name='projects/project-form.html', context=context)


def delete_project(request, pk):
    project_obj = Project.objects.get(id=pk)
    if request.method == 'POST':
        project_obj.title = project_obj.title + " (DELETED)"
        project_obj.active = False
        project_obj.save()

        return redirect('projects-home')
    context = {'object': project_obj}
    return render(request, template_name='projects/delete.html', context=context)


def index(request):
    # developers = MyUser.objects.filter(Q(user_roles='Student') | Q(user_roles='Admin') | Q(user_roles='Teacher'))    # print(developers)
    developers = Profile.objects.all()
    context = {'objects': developers}
    return render(request, template_name='projects/index.html', context=context)