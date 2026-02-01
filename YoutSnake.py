import os
import platform
import time
import subprocess
import sys

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
    import yt_dlp
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

    print("Start donwload")

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download(playlist_links)

    print("done")

def settup():
    os.system('printf "\\033[9;1t"')
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\033[2J\033[H", end="")
    try:
        import yt_dlp
        main()
    except ImportError:
        print("\033[0mWelcome in \033[91mYout\033[92mSnake")
        print("""\033[0mYou dont have libary \033[91m"yt_dlp" """)
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
    if what_OS() in ["Termux", "macOS", "Windows"]:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "yt-dlp"])
    elif what_OS() == "Linux":
        subprocess.check_call([sys.executable, "-m", "pip", "install", "yt-dlp", "--break-system-packages"])
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
        return "macOS"
    elif os_name == "Linux":
        return "Linux"
    else:
        return f"{os_name}"

settup()