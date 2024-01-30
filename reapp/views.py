from django.shortcuts import render, get_object_or_404

from message.models import News
from publication_project.models import Publication, Project, Resource
from team_gallary.models import Team, Gallery


# Create your views here.
def home(request):
    news = News.objects.all()
    data = {'news': news}
    return render(request, 'index.html',data)


def gallery(request):
    gallery = Gallery.objects.all()
    data = {'gallery': gallery}

    return render(request, 'gallary.html', data)


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def projects(request):
    projects = Project.objects.all()
    data = {'projects': projects}
    return render(request, 'project.html', data)


def publications(request):
    publications = Publication.objects.all().order_by('-id')
    data = {'publications': publications}

    return render(request, 'publications.html', data)


def research(request):
    return render(request, 'research.html')


def resources(request):
    resources = Resource.objects.all()
    return render(request, 'resources.html', {'resources': resources})


def resources_details(request, slug):
    resource = get_object_or_404(Resource, slug=slug)
    return render(request, 'resources_de.html', {'resource': resource})


def team(request):
    team = Team.objects.all()
    data = {'team': team}
    return render(request, 'team.html', data)
