import urllib3
import json
import random

class steamapi:
	
	def __init__(self,url,key):
		self.key=key
		self.url=url
		self.http=urllib3.PoolManager()

	def getSteamId(self,vanityname):
		serviceurl=self.url+'/ISteamUser/ResolveVanityURL/v0001/?key='+self.key+'&vanityUrl='+vanityname
		r = self.http.request('GET',serviceurl)
		steamidjson=json.loads(r.data.decode('utf-8'))
		steamid=steamidjson["response"]["steamid"]
		return steamid

	def getGameList(self):
		serviceurl=self.url+'/ISteamApps/GetAppList/v1/?key='+self.key+'&format=json'
		r = self.http.request('GET',serviceurl)
		gamelist=json.loads(r.data.decode('utf-8'))
		return gamelist["applist"]["apps"]["app"]

	def getOwnedGames(self,steamid):
		serviceurl=self.url+'/IPlayerService/GetOwnedGames/v0001/?key='+self.key+'&steamid='+steamid+'&format=json&include_appinfo=1'
		r = self.http.request('GET',serviceurl)
		ogjson=json.loads(r.data.decode('utf-8'))
		return ogjson["response"]["games"]

	def getFullLogoUrl(self,appid,url):
		return 'http://media.steampowered.com/steamcommunity/public/images/apps/'+str(appid)+'/'+url+'.jpg'

	def getAlternateLogoUrl(self,appid):
		return 'http://cdn.akamai.steamstatic.com/steam/apps/'+str(appid)+'/header_292x136.jpg'
