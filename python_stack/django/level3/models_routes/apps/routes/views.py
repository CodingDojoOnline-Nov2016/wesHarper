from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View

# def permission_required(request):
# 	try:
# 		request.session['user_id']


# Create your views here.
class RouteView(View):
	def get(self, request):
		print "get"
		return HttpResponse("You did it")

	def post(self, request):
		print "post"
		return redirect('index')

class UltraView(RouteView):
	statement = "Aaaaahhh this is so Ultra."

	def get(self, request):
		print "get"
		return HttpResponse(self.statement)

	def post(self, request):
		print "post"
		return redirect('index')