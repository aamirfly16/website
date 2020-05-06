from django.shortcuts import render
from .models import Projects

# Create your views here.
def index(request):

    proj1 = Projects()
    proj1.name = 'Point of sale'
    proj1.desc = 'hey'

    proj2 = Projects()
    proj2.name = 'Manage Tenant'
    proj2.desc = 'hey'

    proj3 = Projects()
    proj3.name = 'Crusher Software'
    proj3.desc = 'hey'

    proj4 = Projects()
    proj4.name = 'abc'
    proj4.desc = 'hey'



    return render(request,"index.html", {'proj1':proj1,'proj2':proj2,'proj3':proj3, 'proj4':proj4})