import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from typing import List, Dict

def setup_spotify():
    """Setup Spotify client with user's credentials."""
    print("\n=== Spotify Credentials ===")
    print("(Get these from your Spotify Developer Dashboard)")
    client_id = input("Enter your Spotify Client ID: ")
    client_secret = input("Enter your Spotify Client Secret: ")
    print("\nEnter the EXACT same Redirect URI you added in your Spotify Dashboard")
    redirect_uri = input("Redirect URI: ")
    
    # Create the SpotifyOAuth object
    auth_manager = SpotifyOAuth(
        client_id=client_id,
        client_secret=client_secret,
        redirect_uri=redirect_uri,
        scope="playlist-modify-public playlist-modify-private playlist-read-private user-library-read",
        open_browser=True
    )
    
    return spotipy.Spotify(auth_manager=auth_manager)

def get_playlist_tracks(sp: spotipy.Spotify, playlist_id: str) -> List[Dict]:
    """Get all tracks from a playlist."""
    tracks = []
    results = sp.playlist_tracks(playlist_id)
    
    while results:
        tracks.extend(results['items'])
        if results['next']:
            results = sp.next(results)
        else:
            break
    
    return tracks

def create_split_playlists(sp: spotipy.Spotify, tracks: List[Dict], 
                          chunk_size: int, playlist_name: str):
    """Create new playlists with specified number of tracks."""
    user_id = sp.current_user()['id']
    total_tracks = len(tracks)
    
    # Calculate how many playlists we'll create
    num_playlists = (total_tracks + chunk_size - 1) // chunk_size
    print(f"\nWill create {num_playlists} playlists with {chunk_size} songs each")
    
    for i in range(0, total_tracks, chunk_size):
        # Get the chunk of tracks
        end_idx = min(i + chunk_size, total_tracks)
        chunk = tracks[i:end_idx]
        
        # Create new playlist
        new_name = f"{playlist_name} {i//chunk_size + 1}"
        print(f"\nCreating playlist: {new_name}")
        
        new_playlist = sp.user_playlist_create(
            user_id,
            new_name,
            public=False,
            description=f"Part {i//chunk_size + 1} of split playlist"
        )
        
        # Get track URIs and add them
        track_uris = [
            track['track']['uri'] 
            for track in chunk 
            if track['track'] is not None
        ]
        
        sp.playlist_add_items(new_playlist['id'], track_uris)
        print(f"Added {len(track_uris)} tracks to {new_name}")

def main():
    try:
        # Setup Spotify
        print("=== Spotify Playlist Splitter ===")
        sp = setup_spotify()
        
        # Get playlist URL
        print("\n=== Playlist Information ===")
        playlist_url = input("Enter your Spotify playlist URL: ")
        
        # Extract playlist ID from URL
        playlist_id = playlist_url.split("playlist/")[1].split("?")[0]
        
        # Get playlist details
        playlist = sp.playlist(playlist_id)
        print(f"\nFound playlist: {playlist['name']}")
        print(f"Number of tracks: {playlist['tracks']['total']}")
        
        # Get user preferences
        print("\n=== Split Settings ===")
        songs_per_playlist = int(input("How many songs per playlist? (e.g., 100): "))
        new_name = input("What should we name the new playlists? (e.g., My Split Playlist): ")
        
        # Get all tracks
        print("\nGetting tracks...")
        tracks = get_playlist_tracks(sp, playlist_id)
        
        # Create the split playlists
        create_split_playlists(sp, tracks, songs_per_playlist, new_name)
        
        print("\nDone! Check your Spotify account for the new playlists!")
        
    except Exception as e:
        print(f"\nError: {str(e)}")
        print("\nTips:")
        print("1. Make sure your Spotify Client ID and Secret are correct")
        print("2. Check that your playlist URL is valid")
        print("3. Make sure you're using a number for songs per playlist")

if __name__ == "__main__":
    main()
