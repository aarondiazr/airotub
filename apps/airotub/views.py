from django.shortcuts import render,redirect
from django.http import HttpResponse

import pafy

# Create your views here.

def index(request):
	return render(request,"airotub/index.html")


def GetInfo(request, url):
	try:
		vidobject = pafy.new(url)
		return render(request,"airotub/video.html",{"thumbnail":vidobject.thumb,"titulo":vidobject.title,
			"videodown":"getdown/%s/1"%(url),"audiodown":"getdown/%s/2"%(url),"vale":1})
	except:
		return render(request, "airotub/video.html", {"vale":2})

def GetStream(request,data,data2):
	try:
		vidobject = pafy.new(data)
		best = None
		if(int(data2)==1):
			best = vidobject.getbest(preftype="mp4")
		else:
			best = vidobject.getbestaudio(preftype="ogg")
		return redirect(best.url)
	except:
		return HttpResponse(data2)

def Prueba(request):
	return HttpResponse("hOLA A TODOS")
