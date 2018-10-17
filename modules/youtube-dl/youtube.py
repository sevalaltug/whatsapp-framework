from app.mac import mac, signals
import youtube_dl


@signals.command_received.connect
def handle(message):
    if message.command == "yt":
        mac.send_message("*Kullanımı:* \nVideo için .ytv [youtube-linki]\nMüzik için .ytm [youtube-linki]", message.conversation)
    if message.command == "ytv":
        youtube_video(message)
    if message.command == "ytm":
        youtube_music(message)

'''
Actual module code
==========================================================
'''


def youtube_video(message):
    ydl = {
        'format': 'bestvideo[height<=480]+bestaudio/best[height<=480]',
        'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
        'restrictfilenames': True,
        'noplaylist': True,
        'nocheckcertificate': True,
        'ignoreerrors': False,
        'logtostderr': False,
        'quiet': True,
        'no_warnings': True,
        'default_search': 'auto',
        'source_address': '0.0.0.0',
        'usenetrc': True
    }

    with ydl:
        result = ydl.extract_info(
            'http://www.youtube.com/watch?v=BaW_jenozKc',
            download=False  # We just want to extract the info
        )

    if 'entries' in result:
        # Can be a playlist or a list of videos
        video = result['entries'][0]
    else:
        # Just a video
        video = result

    video_url = video['url']
    mac.send_video(video_url, message.conversaton)
    print(video_url)

def youtube_music(message):
    ydl = {
        'format': 'bestaudio/best',
        'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
        'restrictfilenames': True,
        'noplaylist': True,
        'nocheckcertificate': True,
        'ignoreerrors': False,
        'logtostderr': False,
        'quiet': True,
        'no_warnings': True,
        'default_search': 'auto',
        'source_address': '0.0.0.0',
        'usenetrc': True
    }
