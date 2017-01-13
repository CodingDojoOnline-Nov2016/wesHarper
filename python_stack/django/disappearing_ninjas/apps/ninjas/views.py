from django.shortcuts import render, redirect

# Create your views here.
def index(request):
	return render(request, 'ninjas/index.html')

# def show(request):
# 	return render(request, 'ninjas/show.html')

def ninja(request, color=None):
	static_path = "../static/ninjas/images/{}.jpg" #static files don't like to load variables in django templates

	context = {
		'color': color,
		'images': {
			'donatello': [False, static_path.format("donatello"), "purple"],
			'leonardo': [False, static_path.format("leonardo"), "blue"],
			'michelangelo': [False, static_path.format("michelangelo"), "orange"],
			'raphael': [False, static_path.format("raphael"), "red"],
			'notapril': [False, static_path.format("notapril"), "notapril"]
		},
	}

	color_match = False

	for image, info in context['images'].items():
		if color == info[2]:
			info[0] = True
			color_match = True

	if not color_match:
		if color == None:
			context['images']['donatello'][0] = True
			context['images']['leonardo'][0] = True
			context['images']['michelangelo'][0] = True
			context['images']['raphael'][0] = True
		else:
			context['images']['notapril'][0] = True

	return render(request, 'ninjas/show.html', context)