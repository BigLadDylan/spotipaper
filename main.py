import os
import time 
import subprocess
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from io import BytesIO
# from colorthief import ColorThief 
from PIL import Image, ImageFilter

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id="a6a88604ec1540b29905eeed7ea9829c",
    client_secret="bc0e2458c4b44243bd47dafe1c124715",
    redirect_uri="http://localhost:8080",
    scope="user-read-currently-playing"
))


def album_cover_url():
    current_track = sp.current_user_playing_track()
    if current_track is not None:
        return current_track['item']['album']['images'][0]['url']
    else:
        return None

def create_wallpaper(url):
    if url is not None:
        response = requests.get(url)  # Fetch the album cover image
        response.raise_for_status()  # Ensure the request was successful

        # Open the image from BytesIO
        img = Image.open(BytesIO(response.content))

        # Zoom out by 20%
        zoom_factor = 0.833  # Equivalent to dividing by 1.2
        new_width = int(img.width * zoom_factor)
        new_height = int(img.height * zoom_factor)

        # Resize the image
        img_resized = img.resize((new_width, new_height))

        # Rotate the images
        img_rotated_negative_90 = img_resized.rotate(-90, expand=True)
        img_rotated_90 = img_resized.rotate(90, expand=True)

        new_img = Image.new('RGB', (1920, 1080), (255, 255, 255))

        # Calculate the new size for the images to fill half the canvas width each and the full height
        aspect_ratio = new_height / new_width
        target_height = 1080  # Full height of the canvas
        target_width = int(target_height * aspect_ratio)  # Maintain aspect ratio

        # Resize rotated images to fill the canvas
        img_final_negative_90 = img_rotated_negative_90.resize((target_width, target_height))
        img_final_90 = img_rotated_90.resize((target_width, target_height))

        # Calculate positions for pasting to make them touch each other in the middle
        x_offset_negative_90 = (1920 // 2) - target_width  # Start from the middle and subtract the width
        x_offset_90 = 1920 // 2  # Start from the middle

        # Paste the rotated and resized images
        new_img.paste(img_final_negative_90, (x_offset_negative_90, 0))
        new_img.paste(img_final_90, (x_offset_90, 0))

        # Apply a heavy Gaussian blur to the entire image for color blending
        blurred_img = new_img.filter(ImageFilter.GaussianBlur(radius=25))

        # Define the save path, expanding the user's home directory
        save_path = os.path.expanduser('~/Pictures/WALLPAPERS/current/coverWallpaper.png')
        blurred_img.save(save_path)  # Save the blurred image
        print(f"Image saved to {save_path}")
    else:
        print("No URL to fetch")

def monitor_songs_and_update_wallpaper():
    last_track_id = None  # Initially, there is no last track
    while True:
        current_track = sp.current_user_playing_track()
        if current_track and current_track['item']['id'] != last_track_id:
            print("New song detected, updating wallpaper.")
            url = album_cover_url()
            if url:
                create_wallpaper(url)  # Execute create_wallpaper()
            last_track_id = current_track['item']['id']  # Update last_track_id to the new song's ID
            try:
                subprocess.run(["/home/joebiden/github/spotipaper/wallpaper.sh"], check=True)
                print("swww: wallpaper set!")
            except subprocess.CalledProcessError:
                print("wallpaper.sh FAILED")
        else:
            print("Waiting for the next song...")
        time.sleep(10)  # Check every 10 seconds, adjust as necessary
monitor_songs_and_update_wallpaper()



