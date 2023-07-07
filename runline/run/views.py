from django.shortcuts import render, redirect
from .forms import InputTextForLine
from django.views.decorators.csrf import csrf_exempt
#from .text import video_maker





@csrf_exempt
def create_video(request):
    if request.method == 'POST':
        form = InputTextForLine(request.POST)
        if form.is_valid():
            #video_maker('234')
            form.save()
            return redirect('create_video')

    else:
        form = InputTextForLine()

    return render(
        request,
        'run/video.html',
        {"form": form,
         }
    )