import random
from pytube import YouTube

# Rainbow color codes
colors = [
    "\033[1;31;40m",
    "\033[1;33;40m",
    "\033[1;32;40m",
    "\033[1;34;40m",
    "\033[1;35;40m",
    "\033[1;36;40m",
]

# ASCII art
art = [
	
    " __   __ _____  ____          _    _                    ",
    " \ \ / /|_   _||  _ \  _   _ | |_ | |__    ___   _ __   ",
    "  \ V /   | |  | |_) || | | || __|| '_ \  / _ \ | '_ \  ",
    "   | |    | |  |  __/ | |_| || |_ | | | || (_) || | | | ",
    "   |_|    |_|  |_|     \__, | \__||_| |_| \___/ |_| |_| ",
    "                        |___/                           ",
    "                                                        ",

]

# Print creator in highlighted color
print("\033[1;31;40mCodado by David Mascaro\033[0m")


# Print ASCII art in rainbow colors
for line in art:
    color = random.choice(colors)
    print(color + line)

# Get video URL from user input
url = input("Insira a URL do vídeo seu piratero 💀: ")

# Download video
try:
    video = YouTube(url).streams.get_highest_resolution()
    diretorio = input("Insira o diretorio de onde você deseja salva-lo 💾: ")
    video.download(diretorio)
    print("\033[1;32;40mVideo baixado com sucesso 🔥!\033[0m")
except:
    print("\033[1;31;40mError: Não foi dessa vez, video indisponivel! 💢.\033[0m")
