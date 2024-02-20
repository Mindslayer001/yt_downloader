from django.shortcuts import render
from .models import Yt_Video
from rest_framework.response import Response
from .serializers import VideoSerializer
from rest_framework.decorators import api_view
from pytube import YouTube
import io
from django.http import HttpResponse, HttpResponseServerError
from django.http import FileResponse
from tempfile import TemporaryFile
from pytube import YouTube
import traceback
import logging

@api_view(['GET'])
def getDescription(request):
    params = Yt_Video.objects.all()
    true = True
    false = False
    description = {
    "title": "Django + React Notes App",
    "author": "Dennis Ivy",
    "length": 12240,
    "views": 237475,
    "thumbnail": "https://i.ytimg.com/vi/tYKRAXIio28/hq720.jpg?v=6138bb4c",
    "streams": [
        {
            "mime_type": "video/mp4",
            "type": "video",
            "itag": 18,
            "progressive": true,
            "filesize": 339148153,
            "res": "360p"
        },
        {
            "mime_type": "video/mp4",
            "type": "video",
            "itag": 22,
            "progressive": true,
            "filesize": 624928318,
            "res": "720p"
        },
        {
            "mime_type": "video/mp4",
            "type": "video",
            "itag": 137,
            "progressive": false,
            "filesize": 775400589,
            "res": "1080p"
        },
        {
            "mime_type": "video/webm",
            "type": "video",
            "itag": 248,
            "progressive": false,
            "filesize": 497591046,
            "res": "1080p"
        },
        {
            "mime_type": "video/mp4",
            "type": "video",
            "itag": 136,
            "progressive": false,
            "filesize": 428767930,
            "res": "720p"
        },
        {
            "mime_type": "video/webm",
            "type": "video",
            "itag": 247,
            "progressive": false,
            "filesize": 355734471,
            "res": "720p"
        },
        {
            "mime_type": "video/mp4",
            "type": "video",
            "itag": 135,
            "progressive": false,
            "filesize": 227894284,
            "res": "480p"
        },
        {
            "mime_type": "video/webm",
            "type": "video",
            "itag": 244,
            "progressive": false,
            "filesize": 172026253,
            "res": "480p"
        },
        {
            "mime_type": "video/mp4",
            "type": "video",
            "itag": 134,
            "progressive": false,
            "filesize": 143148097,
            "res": "360p"
        },
        {
            "mime_type": "video/webm",
            "type": "video",
            "itag": 243,
            "progressive": false,
            "filesize": 110172797,
            "res": "360p"
        },
        {
            "mime_type": "video/mp4",
            "type": "video",
            "itag": 133,
            "progressive": false,
            "filesize": 78258588,
            "res": "240p"
        },
        {
            "mime_type": "video/webm",
            "type": "video",
            "itag": 242,
            "progressive": false,
            "filesize": 62751944,
            "res": "240p"
        },
        {
            "mime_type": "video/mp4",
            "type": "video",
            "itag": 160,
            "progressive": false,
            "filesize": 39927738,
            "res": "144p"
        },
        {
            "mime_type": "video/webm",
            "type": "video",
            "itag": 278,
            "progressive": false,
            "filesize": 44304323,
            "res": "144p"
        },
        {
            "mime_type": "audio/mp4",
            "type": "audio",
            "itag": 139,
            "progressive": false,
            "filesize": 74636343,
            "abr": "48kbps"
        },
        {
            "mime_type": "audio/mp4",
            "type": "audio",
            "itag": 140,
            "progressive": false,
            "filesize": 198088101,
            "abr": "128kbps"
        },
        {
            "mime_type": "audio/webm",
            "type": "audio",
            "itag": 249,
            "progressive": false,
            "filesize": 77463752,
            "abr": "50kbps"
        },
        {
            "mime_type": "audio/webm",
            "type": "audio",
            "itag": 250,
            "progressive": false,
            "filesize": 97648511,
            "abr": "70kbps"
        },
        {
            "mime_type": "audio/webm",
            "type": "audio",
            "itag": 251,
            "progressive": false,
            "filesize": 176813870,
            "abr": "160kbps"
        }
    ]
}

    return Response(description)

@api_view(['GET', 'POST'])
def getVideoDescription(request, url):
    link = 'https://www.youtube.com/watch/?v=' + url
    params = fetchLinkDescription(link)
    print("10"+link+"10")
    return Response(params)

def fetchLinkDescription(link):
    youtube_video = YouTube(link)
    description = {
        "title": youtube_video.title,
        "author": youtube_video.author,
        "length": youtube_video.length,
        "views": youtube_video.views,
        "thumbnail": youtube_video.thumbnail_url,
        "streams": extract_stream_info(youtube_video.streams),
    }

    return description

def extract_stream_info(streams):
    stream_info = []
    for stream in streams:
        info = {
            "mime_type": stream.mime_type,
            "type": stream.type,
            "itag": stream.itag,
            "progressive": stream.is_progressive,
            "filesize": stream.filesize,
        }

        # Add 'abr' for audio streams
        if stream.type == "audio":
            info["abr"] = stream.abr
        else:
            info["res"] = stream.resolution

        stream_info.append(info)

    return stream_info


def downloadStream(request, itag, video_id,):
    try:
        video_url = f'https://www.youtube.com/watch?v={video_id}'
        yt = YouTube(video_url)
        stream = yt.streams.itag(itag)

        response = HttpResponse(content_type=stream.mime_type)
        response['Content-Disposition'] = f'attachment; filename="{yt.title}.{stream.subtype}"'

        for chunk in stream.stream_to_buffer(buffer_size=1024*1024):
            response.write(chunk)

        return response
    except Exception as e:
        # Handle errors appropriately
        return HttpResponseServerError(str(e))