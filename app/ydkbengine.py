from app.steamapi import steamapi
import random
import os

class ydkbengine:

	def __init__(self,apikey,vanityname):
		# fetch the steam API key
		self.apikey = apikey
		self.api = steamapi("http://api.steampowered.com",apikey)
		# translate the vanity name into a steamid for further lookups
		self.steamid = self.api.getSteamId(vanityname)
		# cache the full game list and owned game list for future use
		self.allgames = self.api.getGameList()
		self.ownedgames = self.api.getOwnedGames(self.steamid)

	def getUnownedAndUnplayedGames(self):
		uoupgames=[]
		for game in self.allgames:
			if str(game["appid"]) not in self.ownedgames:
				uoupgames.append(game)
		return uoupgames

	def pickOtherGames(self,numgames):
		games=self.getUnownedAndUnplayedGames()
		othergames=[]
		for i in range(0,numgames):
			game = random.choice(games)
			logourl = self.api.getAlternateLogoUrl(game["appid"])
			othergames.append((game["appid"],game["name"],logourl))
		return othergames

	def pickOwnedGame(self,maxplaytime):
		unplayedgames=[]
		for game in self.ownedgames:
			if game["playtime_forever"] <= maxplaytime:
				unplayedgames.append(game)
		game = random.choice(unplayedgames)
		logourl = self.api.getAlternateLogoUrl(game["appid"])
		return (game["appid"],game["name"],logourl)

	def getUnplayedGames(self):
		unplayedgames={}
		for game in self.ownedgames:
			if game["playtime_forever"] == 0:
				unplayedgames[str(game["appid"])] = game["name"]
		return unplayedgames

	def __loadKey(self,file):
		if os.path.isfile(file):
			with open(file,'r') as f:
				key = f.readline().rstrip()
				return key
		else:
			print("Key file ",file," does not exist.")
			raise

