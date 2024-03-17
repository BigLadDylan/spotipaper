#!/bin/zsh

wallpaper=~/Pictures/spotipaper/AlbumCoverWallpaper.png 
album=~/Pictures/spotipaper/AlbumCover.png

current_track_id=""
waybar &
while true; do 
    new_track_id=$(playerctl -p spotify metadata mpris:trackid 2>/dev/null)
    if [ $? -eq 0 ]; then
        if [ "$new_track_id" != "$current_track_id" ]; then

            # Replace with path where you saved the repo.
            python ~/Projects/spotipaper/src/main.py 

            # This applies pywal after wallpaper has generated.
            # Add/remove modules you want applied.
            swww img $wallpaper
            wal -c
            wal --saturate 0.5 -q -i $album 
            pywalfox update
            pywal-discord -t default
            pkill waybar
            waybar &

            current_track_id=$new_track_id
        else
            echo "No new song detected"
        fi
    else
        echo "Spotify is not playing."
        swww img $wallpaper # Dislays previous generated wallpaper.
        current_track_id=""
    fi
    sleep 1
done


