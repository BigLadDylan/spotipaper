 ![spotipaper](https://github.com/BigLadDylan/spotipaper/assets/76881322/f9dad4d4-c2cb-4a75-9c5e-c8e82b51b09d)

Simple python script that beautifully and dynamically changes wallpaper based on current Spotify song playing. 

https://github.com/BigLadDylan/spotipaper/assets/76881322/956ceb7a-2f15-42d2-9dfd-92aeaef8ee9c

This script is the heart of my [dotfiles](https://github.com/BigLadDylan/dotfiles). The script, powered by [pywal](https://github.com/dylanaraps/pywal), transforms a *boring and static* colorscheme to dynamic eye candy with every song that you play.

I love music and chances are that you do too! This is for the melomaniacs out there and perfectly encompasses the customisability of the linux operating system. 


# SETUP
- **DISCLAIMER** This has been tested on Arch Linux with [hyprland](https://hyprland.org/) (wayland). The script is, however, simple enough to easily be adapted to your system. This guide will focus on how to get it working on a similar setup.

The script relies on these following packages:
- AUR: `yay -Syu python python-pywal python-spotipy imagemagick swww pywal-discord pywalfox playerctl`

#### Creating a Spotify app:
1. Assuming you have a spotify account, follow the link to create a developer profile and create a spotify app: https://developer.spotify.com/dashboard. This is to allow the script to interface with the spotify api.
2. Name your app whatever, we are here for the keys. Go into your app's dashboard and copy the `client ID` and `client secret`. Set the redirect link to be `http://localhost:8080`.
   
#### Script configuration
1. Clone this repo wherever.
2. Go into the src/ directory and open `credentials.py`
3. Now paste in the respective details you got from the previous section.
4. Open a new terminal and navigate to the src/ directory and paste these commands to make the scripts executable:
```sh
  chmod +x main.py
  chmod +x wallpaper.sh
```

##### That's it! 🥳 Run `python main.py` whenever you want to generate a wallpaper manually. For extended functionality keep reading:

# Configuration
 will finish later
