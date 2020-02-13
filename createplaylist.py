# Step 1: Log Into Youtube
# # # # # Step 2: Grab Our Liked Videos
#step3: Create A New Playlist
# #Step 4: Search For the Song
#Step : Add this song into the new Spotify Playlist

import json
from secrets import spotify_user_id
class CreatePlaylist:
    def __init__(self):
        self.user_id = spotify_user_id
        self.spotify_token = spotify_token
        self.youtube_client = self.get_youtube_client()

        # step 1: Log Into Youtube
    def get_youtube_client(self):
        os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

        api_service_name = "youtube"
        api_version = "v3"
        client_secrets_file ="client_secret.json"

        scopes =["https://www.googleapis.com/auth/youtube.readonly"]
        flow = google_auth_oauthlib.flow.InstallerAppFlow.from_client_secrets_file(client_secrets_file,scopes)
        credentials = flow.run_console()

        youtube_ client = googleapiclient.discovery.build(api_service_name,api_version,credentials=credentials)

        return youtube_client
    def get_liked_videos(self):
        pass
    def create_playlist(self):
        request_body = json.dump({
           "name": "Youtube Liked Videos",
            "description": "All Liked Youtube Videos",
            "public": True
        })

        query = "https://api.spotify.com/v1/users/{}/playlists".format(self.user_id)
         response = requests.posts(
             query,
             data=request_body,
             headers={
                 "content-type":"application/json",
                 "Authorization":"Bearer {}".format(spotify_token)
             }
         )
        response_json = response.json()
        return response_json["id"]


    # step 4 : search for the Song
    def get_spotify_url(self):
        Query ="https://api.spotify.com/v1/search?query=track%3A{}+artist%3A{}&type=track&offset=0&limit=20".format(
            song_name,
            artist
        )
        response_json = response.json()
        songs =response_json["tracks"]["items"]
        # uses the first song only
        uri =songs[0]["uri"]
        return uri

    #STEP 5 Add the song to the New Spotify Playlist
    def add_song_to_playlist(self):
    self.get_liked_videos()

    uris = []
    for song,info in self.all_song_info.items():
        uris.append(info["spotify_uri"])

        playlist_id = self.create_playlist()

        request_data = json.dumps(uris)
        query ="https://api.spotify.com/v1/playlists/{}/tracks".format(playlist_id)
         response = requests.post(
          query,
          data=request_data,
           headers={
          "Content-Type": "application/json",
          "Authorization": "Bearer {}".format(self.spotify_token)
    }
)
        response_json =response.json()
        return response_json