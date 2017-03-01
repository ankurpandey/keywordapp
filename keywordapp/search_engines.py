import json
import urllib.request as ur

class SearchEngines(object):
	"""docstring for SearchEngines"""
	
	def commonProcess(self,url,query):
		query = query.replace(" ","+")
		final_url = url + query
		response = ur.urlopen(final_url)
		data = json.loads(response.read().decode("utf8"))
		results = data[1]
		return results

	def googleEngine(self, query):
		url = "https://www.google.co.in/complete/search?client=firefox&q="
		return self.commonProcess(url,query)

	
	def bingEngine(self, query):
		url = "http://api.bing.com/osjson.aspx?query="
		return self.commonProcess(url,query)


	def yahooEngine(self, query):
		url = "http://sugg.search.yahoo.net/sg/?output=jsonp&command="
		query = query.replace(" ","+")
		final_url = url + query
		response = ur.urlopen(final_url)
		temp_json = response.read().decode('utf8').replace('(',"").replace(')',"")
		data = json.loads(temp_json)
		temp_arr = data["gossip"]["results"]
		keywords_list = []
		for item in temp_arr:
			keywords_list.append(item["key"])
		return keywords_list
		
	