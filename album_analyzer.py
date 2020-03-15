import matplotlib.pyplot as plt

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

class Album:
	"""
	Store all the necessary information for an album, including album name,
	album ID, album image URL, and information about all the tracks.
	"""
	def __init__(self, album_id):
		album_info = spotify.album(album_id)
		self.id = album_id
		self.name = album_info['name']
		self.artists = [artist['name'] for artist in album_info['artists']]
		self.image_url = album_info['images'][0]['url']
		self.track_ids = [track['id'] for track in album_info['tracks']['items']]
		self.track_names = [track['name'] for track in album_info['tracks']['items']]
		self.track_audio_features = spotify.audio_features(tracks=self.track_ids)

def get_album(album_id):
	return Album(album_id)

def plot_feature(album, feature):
	"""
	Takes in an Album object and the name of an audio feature (str).
	Plots the value of the feature across the album.
	"""
	plt.plot(album.track_names, [track[feature] for track in album.track_audio_features])
	plt.xticks(rotation=60, horizontalalignment='right')
	plt.ylabel(feature)
	plt.title(album.name)
	plt.tight_layout()
	plt.show()