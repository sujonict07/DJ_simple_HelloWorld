# Create your views here.
#from django.http import HttpResponse
from django.shortcuts import render_to_response
def foo(request,):
	#name = "sujon"
	#html = "<html><body>Hello World! from %s</body></html>" % name
	
	return render_to_response("helloDJ/home.html",
			{"Testing":"Django Template Inheritance",
			"HelloHello":"Hello World - Django"
			}
		);
