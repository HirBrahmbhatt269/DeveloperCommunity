from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Project
from .forms import ProjectForm

project_dictionary = [
    {'id':'1','name':'The song of Achilles', 'Author': 'Madilyn', 'pages' : 120},
    {'id':'2','name':'Seven Husbands of Evelyn Hugo', 'Author': 'Unknown', 'pages' : 700},
    {'id':'3','name':'Into Thin Air', 'Author': 'John Krakauer', 'pages' : 225},
]

# Create your views here.
def projects(request):
    #The third parameter which you can add to render function is called context.
    # Basically you can pass some value from views to template using the jinja tags. Like page name below...
    # So basically, you will be able to access page variable's value in projects.html using project_page variable name.
    list = ['Circe', 'Kusum', 'Indira']
    number = 10
    page = "projects"
    projectList = Project.objects.all()
    context = {'names': list,'page': page,'number': number, 'projectDict' : project_dictionary, 'projectList': projectList}
    #If you have a map like context above, then just pass the map. Basically you need to pass the key-value pair as context in render
    return render(request, 'projects/projects.html',context)

def singleproject(request, pk):
    projectObj = Project.objects.get(id=pk)
    # None is basically null in python
    for i in project_dictionary:
        if i['id'] == str(pk):
            projectObj = i
    return render(request, 'projects/single-project.html', {'project' : projectObj})

def woparam(request):
    return HttpResponse('Let\'s see what a function without param looks...' + str(request) + "You wont see the request here!but I passed it")

def createProject(request):
    form = ProjectForm()
    if request.method=='POST':
        form = ProjectForm(request.POST) # this post request will basically have the attributes and all
        if form.is_valid():
            form.save()
            return redirect('projects')
    context = {'form': form}
    return render(request, 'projects/projects-form.html', context)


def updateProject(request,pk):
    updproject = Project.objects.get(id=pk)
    form = ProjectForm(instance=updproject)
    if request.method=='POST':
        form = ProjectForm(request.POST, instance = updproject) # this post request will basically have the attributes and all
        if form.is_valid():
            form.save()
            return redirect('projects')
    context = {'form': form}
    return render(request, 'projects/projects-form.html', context)

def deleteProject(request, pk):
    project = Project.objects.get(id = pk)
    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    context = {'object': project}
    return render(request, 'projects/delete-template.html', context)