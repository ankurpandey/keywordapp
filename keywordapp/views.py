from django.shortcuts import render
from keywordapp.search_engines import SearchEngines

def appindex(request):
	error = False
	if 'q' in request.GET:
		q = request.GET['q']
		engine = SearchEngines()
		google = engine.googleEngine(q)	
		bing = engine.bingEngine(q)	
		yahoo = engine.yahooEngine(q)
		if not 'q':
			error = True
		else:
			return render(request,'index.html',{'query':q, 'results_google':google,'results_bing':bing,'results_yahoo':yahoo})
	return render(request, 'index.html')

