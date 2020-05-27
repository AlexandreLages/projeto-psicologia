from django.shortcuts import render


def blog_view(request):
	if request.method == 'GET':
		return render(request, 'index.html')
