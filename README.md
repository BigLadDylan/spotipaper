 ![spotipaper](https://github.com/BigLadDylan/spotipaper/assets/76881322/f9dad4d4-c2cb-4a75-9c5e-c8e82b51b09d)

Simple python script that beautifully and dynamically changes wallpaper based on current Spotify song playing. 

This script is the heart of my [dotfiles](https://github.com/BigLadDylan/dotfiles). The script, powered by [pywal](https://github.com/dylanaraps/pywal), transforms a *boring and static* colorscheme to dynamic eye candy with every song that you play.

# SETUP
- **DISCLAIMER** This has been tested on Arch Linux with [hyprland](https://hyprland.org/) (wayland). The script is, however, simple enough to easily be adapted to your system. This guide will focus on how to get it working on a similar setup.

#### Installation
**AUR** (Arch):
```
yay -Syu python python-pywal python-spotipy imagemagick swww pywal-discord pywalfox playerctl
```

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

<details>
  <summary>❗ LIMITATIONS ❗</summary>
Works perfectly with a few caveats: 
 
- Designed for 1920x1080 resolution. Higher resolutions will require upscaling the wallpaper, not a breaking limitation but your milage may vary (Can be changed if you fiddle with `main.py`
- `Wal cannot generate a pallet` for albums with mostly one color, rare occurance. It will just use the previous song's pallet.
- Sometime's albums fetched do not match the album that your client displays. This is due to the way in which artists reupload their music under different album covers eg: anniversary versions.  
  
</details>


