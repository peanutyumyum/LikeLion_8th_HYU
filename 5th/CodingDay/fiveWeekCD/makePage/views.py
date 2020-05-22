from django.shortcuts import render
from .models import youTubeChannel

# Create your views here.

def home(request):
    youTube1 = youTubeChannel.objects.get(id=1)
    youTube2 = youTubeChannel.objects.get(id=2)
    youTube3 = youTubeChannel.objects.get(id=3)
    return render(request, 'home.html',{'youtube1':youTube1, 'youtube2':youTube2, 'youTube3':youTube3})