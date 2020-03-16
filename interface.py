import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

from album_analyzer import *

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

FEATURES = [
	'acousticness',
	'danceability',
	'energy',
	'instrumentalness',
	'liveness',
	'loudness',
	'speechiness',
	'valence',
	'tempo',
]

def main():
	while True:
		# search for an album
		q = input("Name of the album to search for (or 'quit' to exit): ")
		if q == 'quit':
			break

		results = spotify.search(q, type='album')
		names = [item['name'] for item in results['albums']['items']]
		for i in range(len(names)):
			print("%s %s" % (i+1, names[i]))

		# choose one of the results
		inp = input("Enter the number of your selection, or 'cancel' to cancel: ") 
		if inp == 'cancel':
			continue

		try:
			idx = int(inp) - 1
		except ValueError:
			print("Invalid value: %s" % inp)
			continue

		album = get_album(results['albums']['items'][idx]['id'])

		# get feature to plot
		feature = input("Enter the feature you want to plot. Options are: \n\t%s\n" %
						'\n\t'.join(FEATURES))
		if feature not in FEATURES:
			print("Invalid value: %s" % feature)
			continue

		plot_feature(album, feature)

if __name__ == "__main__":
    main()
