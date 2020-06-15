# std lib
import os
# import sys

# own
from utils import read_playlist_name
from utils import get_authenticated_service
from utils import CLIENT_SECRETS_FILE
from utils import SCOPES
from utils import TOKEN_PLAYLIST_FILE


def remove_empty_kwargs(**kwargs):
    good_kwargs = {}
    if kwargs is not None:
        for key, value in kwargs.items():
            if value:
                good_kwargs[key] = value
    return good_kwargs


def playlists_insert(dirpath, client, **kwargs):
    # resource = build_resource(properties)
    kwargs = remove_empty_kwargs(**kwargs)
    title = read_playlist_name(dirpath)

    response = client.playlists().insert(
        body={
            "snippet": {
                "title": title,
                "description": "",
                "tags": [
                    "sample playlist",
                    "API call"
                ],
                "defaultLanguage": "en"
            },
            "status": {
                "privacyStatus": "private"
            }
        },
        **kwargs
    ).execute()

    print(response)
    return response


def create_playlist(directory):
    # nom de la playlist
    # if len(sys.argv) == 1:
        # dirpath = os.getcwd()
    # else:
        # dirpath = sys.argv[1]

    # créer le client
    client = get_authenticated_service(CLIENT_SECRETS_FILE, TOKEN_PLAYLIST_FILE, SCOPES)

    # créer une playlist vide ?
    response = playlists_insert(directory,
                                client,
                                part='snippet,status',
                                onBehalfOfContentOwner='')

    id_playlist = response['id']
    # uploader chaque vidéo en lui donnant la bonne id

    return id_playlist

if __name__ == '__main__':
    create_playlist(os.getcwd())
