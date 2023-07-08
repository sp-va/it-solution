from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import InputTextForLine
from django.views.decorators.csrf import csrf_exempt
from .video_maker import video_maker



@csrf_exempt
def create_video(request):
    if request.method == 'POST':
        form = InputTextForLine(request.POST)
        if form.is_valid():
            video_maker(form.cleaned_data['text'])
            form.save()
            with open('./static/run/output_video.avi', 'rb') as out:
                response = HttpResponse(out.read(), content_type='video/avi')
                response['Content-Disposistion'] = 'attachment; filename=output_video.avi'
                return response
    else:
        form = InputTextForLine()

    return render(
        request,
        'run/video.html',
        {"form": form,
         }
    )

