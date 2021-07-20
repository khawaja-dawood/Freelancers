from django.shortcuts import render
from django.http import HttpResponse
from .models import Project, Tag, Review


projectsList = [
    {
        'id': '1',
        'title': 'Ecommerce Website',
        'description': 'Fully functional ecommerce website',
        'topRated': True
    },
    {
        'id': '2',
        'title': 'Portfolio Website',
        'description': 'A personal website to write articles and display work',
        'topRated': False
    },
    {
        'id': '3',
        'title': 'Social Network',
        'description': 'An open source project built by the community',
        'topRated': True
    }
]


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