import os
import platform
import time
import subprocess

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
    print("""\033[0m1.) Download \033[94mmp3""")
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
        print("Welcome in YoutSnake")
        print("""You dont have libary "yt_dlp" """)
        print("Start download")
        y_or_n = input(""""y"/"n" """)
        if y_or_n == "y":
            download_libary()
        elif y_or_n == "n":
            print("Without libarys you cant download things")
            print("Starting YoutSnake on visulation mode...")
            time.sleep(2)
            main()
        else:
            print("""Type only "y" or "n" """)
            time.sleep(1)
            settup()

def download_libary():
    print("\033[0mDevice OS: \033[92m" + what_OS())
    if what_OS == "Termux":
        cmd = ["pip", "install", "yt-dlp"]
    if what_OS == "Linux":
        cmd = ["pip", "install", "yt-dlp", "--break-system-packages"]
    


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