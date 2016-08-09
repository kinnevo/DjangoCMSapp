from django.shortcuts import render, render_to_response
from .models import Activity
import sys

# Create your views here.
def demo(request):
#    print( "00000000000000000000000000000000000000000000000", sys.path)
#    print( "Views in Capture", request.app_path)
    activities = Activity.objects.all()
#    return render_to_response( 'demo.html')
    return render( request, 'demo.html', {'activities': activities})

