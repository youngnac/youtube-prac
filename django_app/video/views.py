import json

import requests
from dateutil.parser import parse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect

from utils.settings import search_conf
from video.forms import SearchForm
from video.models import VideoInfo


def search_single_video(video_id):
    key_ = search_conf()
    r_key = key_['youtube']['API_KEY']
    part = "snippet"
    id = video_id
    my_param = {
        'part': part,
        'id': id,
        'key': r_key,
    }
    youtube_single_url = "https://www.googleapis.com/youtube/v3/videos"
    r = requests.get(youtube_single_url, params=my_param)
    r_text = json.loads(r.text)
    item = r_text["items"]
    for index, i in enumerate(item):
        title = i["snippet"]["title"]
        channel_id = i["snippet"]["channelId"]
        channel_title = i["snippet"]["channelTitle"]
        p_d = i["snippet"]["publishedAt"]
        published_date = parse(p_d)
        thumbnail = i["snippet"]['thumbnails']["default"]["url"]
        single_dict = {'title': title,
                       'video_id': video_id,
                       'channel_id': channel_id,
                       'channel_title': channel_title,
                       'published_date': published_date,
                       'thumbnail': thumbnail}
        return single_dict


def search_youtube(keyword, num, page_token=None):
    # current_pwd = os.path.abspath(__file__)
    # conf = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(current_pwd))), '.conf')
    # key_ = json.loads(open(os.path.join(conf, 'settings_local.json')).read())
    key_ = search_conf()
    part = "snippet"
    keyword = keyword
    r_key = key_['youtube']['API_KEY']
    num = num
    my_param = {
        'part': part,
        'q': keyword,
        'key': r_key,
        'maxResults': num,
        'type': 'video',
        'pageToken': page_token
    }
    youtube_url = "https://www.googleapis.com/youtube/v3/search"
    r = requests.get(youtube_url, params=my_param)
    r_text = json.loads(r.text)
    item = r_text["items"]
    nxt_pg = r_text.get("nextPageToken")
    prev_pg = r_text.get("prevPageToken")

    v_list = []

    for index, i in enumerate(item):
        title = i["snippet"]["title"]
        # title_list.append(title)
        video_id = i["id"]["videoId"]
        # video_list.append(video_id)
        channel_id = i["snippet"]["channelId"]
        # channel_id_list.append(channel_id)
        channel_title = i["snippet"]["channelTitle"]
        # channel_list.append(channel_title)
        p_d = i["snippet"]["publishedAt"]
        published_date = parse(p_d)
        # obj_str = "obj {}".format(index)
        thumbnail = i["snippet"]['thumbnails']["default"]["url"]
        v_list.append({'title': title,
                       'video_id': video_id,
                       'channel_id': channel_id,
                       'channel_title': channel_title,
                       'published_date': published_date,
                       'keyword': keyword,
                       'thumbnail': thumbnail})

    return v_list, nxt_pg, prev_pg,


def search_video_view(request):
    if request.GET.get('keyword', '').strip() != "":
        form = SearchForm(request.GET)
        if form.is_valid():
            keyword = form.cleaned_data["keyword"]
            num = form.cleaned_data["num"]
            page_token = request.GET.get("page_token")
            v_list, nxt_pg, prev_pg = search_youtube(keyword, num, page_token)
            user_list = request.user.my_video.values_list("video_id", flat=True)
            context = {
                'keyword': keyword,
                'form': form,
                'list': v_list,
                'nxt_pg': nxt_pg,
                'prev_pg': prev_pg,
                'num': num,
                'user_box': user_list,
            }
            # request.get_full_path()
            return render(request, 'video/search.html', context)
    else:
        context = {
            'form': SearchForm()
        }
        return render(request, 'video/search.html', context)


@login_required
def video_add_view(request, video):
    if request.method == "POST":
        user = request.user
        video_info = search_single_video(video)
        path = request.POST["path"]
        VideoInfo.objects.get_or_create(title=video_info["title"],
                                        channel_title=video_info["channel_title"],
                                        channel_id=video_info["channel_id"],
                                        video_id=video,
                                        published_date=video_info["published_date"], )
        user.add_to_box(VideoInfo.objects.get(video_id=video))
        prev_path = path

        return redirect(prev_path)


@login_required
def remove_view(request, video):
    if request.method == "POST":
        user = request.user
        user.my_video.get(video_id=video).delete()
        return redirect('member:my-box')


@login_required
def search_remove_view(request, video):
    if request.method == "POST":
        user = request.user
        user.my_video.get(video_id=video).delete()
        path = request.POST["path"]
        prev_path = path
        return redirect(prev_path)

def bookmark_list(request):
    all_bookmarks = request.user.bookmark_set.select_related('video')
    paginator = Paginator(all_bookmarks, 5)
    page = request.GET.get["page"]
    try:
        bookmarks = paginator.page(page)
    except PageNotAnInteger:
        bookmarks = paginator.page(1)
    except EmptyPage:
        bookmarks = paginator.page(paginator.num_pages)

    context = {
        'bookmarks': bookmarks,
    }
    return render(request, 'video/bookmark_list.html', context)
