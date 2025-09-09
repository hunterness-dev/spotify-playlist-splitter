# spotify-playlist-splitter
# Spotify Playlist Splitter

Split your big Spotify playlists into smaller ones!

## Quick Start

1. Set up your Spotify App:
   - Go to [Spotify Developer Dashboard](https://developer.spotify.com/dashboard)
   - Click "Create App"
   - Choose any App name and description
   - Add a Redirect URI in your app settings (example: http://localhost:8888/callback)
   - Save the Redirect URI exactly as you entered it
   - Copy your Client ID and Client Secret

2. Install spotipy:
   ```
   pip install spotipy
   ```

3. Run the script:
   ```
   python playlist_splitter.py
   ```

## How to Use

1. Enter your Spotify Client ID and Secret
2. Paste your playlist URL
3. Choose how many songs you want in each playlist
4. Enter a name for your new playlists

Example:
```
=== Spotify Playlist Splitter ===
Enter your Spotify Client ID: (your client id)
Enter your Spotify Client Secret: (your client secret)
Enter the EXACT same Redirect URI you added in your Spotify Dashboard
Redirect URI: http://localhost:8888/callback

=== Playlist Information ===
Enter your Spotify playlist URL: https://open.spotify.com/playlist/...

Found playlist: My Big Playlist
Number of tracks: 350

=== Split Settings ===
How many songs per playlist? (e.g., 100): 100
What should we name the new playlists? (e.g., My Split Playlist): Summer Mix

Creating playlist: Summer Mix 1
Creating playlist: Summer Mix 2
Creating playlist: Summer Mix 3
Creating playlist: Summer Mix 4

Done! Check your Spotify account for the new playlists!
```

That's it! Your new playlists will appear in your Spotify account.

