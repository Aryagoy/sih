from django.shortcuts import render

from django.http import JsonResponse

def blog_list(request):
	context = {
		'name': 'some title here',
		'description': 'some description as well'
	}
	return JsonResponse(context)




def home(request):
	return render(request, "rest_insurance/index.html", {})

def homepage(request):
    return render(request,"login/base.html")

def login(request):
    return render(request,"login/login.view.html")
