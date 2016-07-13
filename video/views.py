from django.shortcuts import render
from .models import Video

def video_list(request):
    videos = Video.objects.all()
    return render(request, 'video/video_list.html', {'videos': videos})

def video(request, video_id):
    video = Video.objects.get(id=int(video_id))
    return render(request, 'video/video.html', {'video': video})
