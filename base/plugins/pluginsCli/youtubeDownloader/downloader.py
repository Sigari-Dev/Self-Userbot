import youtube_dl
ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s.%(ext)s'})

def extract_info(url):
    with ydl:
        result = ydl.extract_info(
            'https://www.youtube.com/watch?v=16IbrAvYRBw',
            download=False # We just want to extract the info
        )

        formats = result.get('formats', result) 
    return sorted(formats, key=lambda x: x['quality'])