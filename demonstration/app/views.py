from django.shortcuts import render, HttpResponse
import requests
import json

# Create your views here.
def index(request):
	return HttpResponse('Hello world')

def test(request):
	return HttpResponse('My second view')

def profile(request):
	parsedData = []
	if request.method == 'POST':
		username = request.POST.get('user')
		jsonList = []
		req = requests.get('https://api.github.com/users/' + username)
		jsonList.append(json.loads(req.content.decode('utf-8')))
		# jsonReturned = json.loads(req.content.decode('utf-8'))
		userData = {}
		for data in jsonList:
			userData['name'] = data['name']
			userData['blog'] = data['email']
			userData['public_gists'] = data['public_gists']
			userData['public_repos'] = data['public_repos']
			userData['avatar_url'] = data['avatar_url']
			userData['followers'] = data['followers']
			userData['following'] = data['following']
			parsedData.append(userData)
	# return HttpResponse(parsedData)
	return render(request, 'app/profile.html', {'data': parsedData})
