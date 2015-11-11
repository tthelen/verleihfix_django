from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Thing


def home(request):
    thing_list = Thing.objects.all()
    return render(request, 'things.tmpl', {'thing_list': thing_list})

def lend(request):
    try:
        thing = Thing.objects.get(id=request.POST['thing'])
    except KeyValue:
        return HttpResponse(code=404)

    return HttpResponse(json.dumps({ok:false}), content_type='application/json')

#def save(request):
#    from django.utils import timezone
#   try:
#       if request.user.is_authenticated():
#           author = request.user
#       else:
#           author = None
#       tweet = Tweet(message=request.POST['status'], mkdate=timezone.now(), author=author)
#       tweet.save()
#       messages.info(request, 'The message was saved.')
#   except KeyError:
#       messages.error(request, 'Error: No message given.')
#   return redirect("/")

