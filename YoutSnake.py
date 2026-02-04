import os
import platform
import time
import subprocess
import sys
import shutil
import yt_dlp

def main():
    os.system('printf "\\033[9;1t"')
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\033[2J\033[H", end="")
    print("""
\033[91m█████ █████                      █████     \033[92m█████████                       █████              
\033[91m▒▒███ ▒▒███                      ▒▒███     \033[92m███▒▒▒▒▒███                     ▒▒███               
\033[91m ▒▒███ ███    ██████  █████ ████ ███████  \033[92m▒███    ▒▒▒  ████████    ██████   ▒███ █████  ██████ 
\033[91m  ▒▒█████    ███▒▒███▒▒███ ▒███ ▒▒▒███▒   \033[92m▒▒█████████ ▒▒███▒▒███  ▒▒▒▒▒███  ▒███▒▒███  ███▒▒███
\033[91m   ▒▒███    ▒███ ▒███ ▒███ ▒███   ▒███     \033[92m▒▒▒▒▒▒▒▒███ ▒███ ▒███   ███████  ▒██████▒  ▒███████ 
\033[91m    ▒███    ▒███ ▒███ ▒███ ▒███   ▒███ ███ \033[92m███    ▒███ ▒███ ▒███  ███▒▒███  ▒███▒▒███ ▒███▒▒▒  
\033[91m    █████   ▒▒██████  ▒▒████████  ▒▒█████ \033[92m▒▒█████████  ████ █████▒▒████████ ████ █████▒▒██████ 
\033[91m   ▒▒▒▒▒     ▒▒▒▒▒▒    ▒▒▒▒▒▒▒▒    ▒▒▒▒▒   \033[92m▒▒▒▒▒▒▒▒▒  ▒▒▒▒ ▒▒▒▒▒  ▒▒▒▒▒▒▒▒ ▒▒▒▒ ▒▒▒▒▒  ▒▒▒▒▒▒                                                                                                                                                                                                
                                                                                               """)
    print("\033[0mAuthor: @patriq128")
    print("\033[91m!!!For personal use only!!!")
    print("""\033[0m*type "exit" for exit :3 """)
    print("\033[0mDevice OS: \033[92m" + what_OS())
    print("\033[0m----------------------------------------------------------------------------------------------------")
    print("""\033[0m1.) Download \033[94mMP3""")
    print("\033[0m----------------------------------------------------------------------------------------------------")
    choose_main = input("\033[0mChoose option:")

    if choose_main == "1":
        mp3down()
    elif choose_main == "exit":
        exit()
    else:
        print("\033[91m!Wrong Input")
        time.sleep(1)
        main()

def mp3down():
    os.system('printf "\\033[9;1t"')
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\033[2J\033[H", end="")
    print("""\033[94m ██████   ██████ ███████████   ████████ 
░░██████ ██████ ░░███░░░░░███ ███░░░░███
 ░███░█████░███  ░███    ░███░░░    ░███
 ░███░░███ ░███  ░██████████    ██████░ 
 ░███ ░░░  ░███  ░███░░░░░░    ░░░░░░███
 ░███      ░███  ░███         ███   ░███
 █████     █████ █████       ░░████████ 
░░░░░     ░░░░░ ░░░░░         ░░░░░░░░                                                                    
                                        """)
    print("""\033[92m                                                                
▄█████ ▄▄  ▄▄  ▄▄▄  ▄▄ ▄▄ ▄▄▄▄▄ 
▀▀▀▄▄▄ ███▄██ ██▀██ ██▄█▀ ██▄▄  
█████▀ ██ ▀██ ██▀██ ██ ██ ██▄▄▄ 
                                \033[0m""")
    print("""*Paste link, click enter and you can paste another link and when you`re done just type "ok".""")
    print("\033[0m----------------------------------------------------------------------------------------------------")
    playlist_links = []

    while True:
        link = input("> ").strip()
        if link.lower() == "ok":
            break
        if link:
            playlist_links.append(link)
        if link.lower() == "exit":
            exit()

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

    print("Start download")

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download(playlist_links)

    print("done")

def settup():
    os.system('printf "\\033[9;1t"')
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\033[2J\033[H", end="")
    try:
        import yt_dlp
        if is_ffmpeg():
            main()
        else:
            print("""\033[0mYou dont have \033[91m"ffmpeg" """)
            print("\033[92mStart download?")
            ffmpeg_input = input("""\033[92m"y"\033[0m/\033[91m"n"\033[0m: """)
            if ffmpeg_input == "y":
                download_ffmpeg()
            elif y_or_n == "n":
            print("\033[91mWithout ffmpeg its dont gonna work")
            print("\033[0mExiting...")
            time.sleep(2)
            exit()
        else:
            print("""\033[0mType only \033[92m"y" \033[0mor \033[91m"n" """)
            time.sleep(1)
            settup()
                
    except ImportError:
        print("\033[0mWelcome in \033[91mYout\033[92mSnake")
        print("""\033[0mYou dont have libary \033[91m"yt_dlp" """)
        if not is_ffmpeg():
            print("""\033[0mAnd \033[91m"ffmpeg" """)    
        print("\033[92mStart download?")
        y_or_n = input("""\033[92m"y"\033[0m/\033[91m"n"\033[0m: """)
        if y_or_n == "y":
            download_libary()
        elif y_or_n == "n":
            print("\033[91mWithout libarys its dont gonna work")
            print("\033[0mExiting...")
            time.sleep(2)
            exit()
        else:
            print("""\033[0mType only \033[92m"y" \033[0mor \033[91m"n" """)
            time.sleep(1)
            settup()

def download_libary():
    print("\033[0mDevice OS: \033[92m" + what_OS() + "\033[94m")
    if what_OS() in ["Termux", "MacOS", "Windows"]:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "yt-dlp"])
    elif what_OS() == "Linux":
        subprocess.check_call([sys.executable, "-m", "pip", "install", "yt-dlp", "--break-system-packages"])
    else:
        print("\033[91mSorry, something went wrong")
    
    print("\033[91mDone")
    time.sleep(1)
    main()

def download_ffmpeg():
    print("\033[0mDevice OS: \033[92m" + what_OS() + "\033[94m")
    if what_OS() == "Linux":
        subprocess.check_call(["sudo", "apt", "install", "-y", "ffmpeg"])
    elif what_OS() == "Termux":
        subprocess.check_call(["pkg", "install", "-y", "ffmpeg"])
    elif what_OS() == "MacOS":
        subprocess.check_call(["brew", "install", "ffmpeg"])
    elif what_OS() == "Windows":
        import urllib.request
        import zipfile
        url = "https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip"
        zip_path = "ffmpeg.zip"
        extract_path = "ffmpeg"
        urllib.request.urlretrieve(url, zip_path)

        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_path)
        ffmpeg_bin = os.path.join(extract_path, "ffmpeg-release-essentials", "bin", "ffmpeg.exe")
        print(ffmpeg_bin)
    else:
        print("\033[91mSorry, something went wrong")

    print("\033[91mDone")
    time.sleep(1)
    main()


def what_OS():
    if "TERMUX_VERSION" in os.environ or os.path.exists("/data/data/com.termux"):
        return "Termux"

    os_name = platform.system()

    if os_name == "Windows":
        return "Windows"
    elif os_name == "Darwin":
        return "MacOS"
    elif os_name == "Linux":
        return "Linux"
    else:
        return f"{os_name}"

def is_ffmpeg():
    return shutil.which("ffmpeg") is not None

settup()