# coding: utf-8
import os
import json
import requests
import urllib.request
#import requests

folder = "NamedImages"

if not os.path.exists(folder):
	os.mkdir(folder)

# extract scryfall card ids from allcards.json
with open('AllCards.json') as f:
	all_mtg_cards = json.load(f)
	# make mapping of name to scryfall id
	planechase_cards = {}

	for card in all_mtg_cards:
		if all_mtg_cards[card]["layout"] == "planar":
			planechase_cards[card] = all_mtg_cards[card]["scryfallId"]

	base_url = "https://api.scryfall.com/cards/"

	for card in planechase_cards:
		url = base_url + planechase_cards[card]
		r = requests.get(url)
		data = r.json()

		image_url = data["image_uris"]["border_crop"]
		urllib.request.urlretrieve(image_url, folder + "/" + card + "@x3.png")


