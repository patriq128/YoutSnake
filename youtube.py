import yt_dlp

playlist_links = []

while True:
    link = input("> ").strip()
    if link.lower() == "ok":
        break
    if link:
        playlist_links.append(link)

if not playlist_links:
    print("exit")
    exit()

ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': 'Music/%(playlist_title)s/%(title)s.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'ignoreerrors': True,
    'quiet': False,
}

print("Start donwload")

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download(playlist_links)

print("done")
