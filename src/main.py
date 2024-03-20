from credentials import clientID, clientSecret, redirectURI
import os
import requests
from io import BytesIO
from PIL import Image, ImageFilter, ImageEnhance
import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id = clientID,
    client_secret = clientSecret,
    redirect_uri = redirectURI,
    scope = "user-read-currently-playing"  
))

def FetchURL():
    current_track = sp.current_user_playing_track()
    if current_track:
        url = current_track['item']['album']['images'][0]['url']
        return url
    else:
        print("None")
        return None

def CreateWallpaper():
    url = FetchURL()
    if url is not None:
        response = requests.get(url)  # Fetch the album cover image
        response.raise_for_status()  # Ensure the request was successful
        img = Image.open(BytesIO(response.content))
        savePath = os.path.expanduser('~/Pictures/spotipaper/AlbumCover.png')
        os.makedirs(os.path.dirname(savePath), exist_ok=True)
        img.save(savePath)  # Save the blurred image

        enhancer = ImageEnhance.Color(img)
        img_saturated = enhancer.enhance(2.0)  # Increase saturation; 2.0 is a sample factor for more vivid colors

        # Zoom out by 20%
        zoom_factor = 0.833  # Equivalent to dividing by 1.2
        new_width = int(img_saturated.width * zoom_factor)
        new_height = int(img_saturated.height * zoom_factor)

        # Resize the image
        img_resized = img_saturated.resize((new_width, new_height))

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
        save_path = os.path.expanduser('~/Pictures/spotipaper/AlbumCoverWallpaper.png')
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        blurred_img.save(save_path)  # Save the blurred image
    else:
        print("No URL to fetch")
CreateWallpaper()
