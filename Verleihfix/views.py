from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils.datastructures import MultiValueDictKeyError
from django.core.exceptions import ValidationError
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Category, Type, Thing, Lending
from datetime import datetime


def d(request_date):
    """Converts a date from a request in yyyy-mm-dd format to a datetime.date"""
    return datetime.strptime(request_date, "%Y-%m-%d").date()


def home(request):
    """List all available things."""
    # TODO: Filtering, searching
    category_list = Category.objects.all()
    return render(request, 'things.tmpl', locals())


@login_required
def lend(request):
    """Try to lend a thing. Request must contain thing id, startdate and enddate."""

    try: # extract and check request parameters
        type = Type.objects.get(id=request.GET['type'])
        #thing = Thing.objects.get(id=request.GET['thing'])
        startdate = d(request.GET['startdate_submit'])
        enddate = d(request.GET['enddate_submit'])
    except (ValueError, MultiValueDictKeyError):
        return HttpResponse(status=400, content="Insufficient data.")

    try:  # use model to lend thing
        things = type.available_things(startdate,enddate)
        if len(things) > 0 and things[0].lend(request.user, startdate, enddate, status="reserved"):
            messages.success(request, 'Ausleihvorgang erfolgreich. Das Gerät wurde reserviert. Bitte holen Sie es am %s ab.' % enddate)
            return redirect("lendings")
            # return HttpResponse(json.dumps({'ok':True}),
            #                    content_type='application/json')

        else:
            messages.error(request, 'Das Gerät konnte nicht reserviert werden.')
            return redirect("home")
            # return HttpResponse(json.dumps({'ok':False, 'reason':"Buchung nicht möglich."}),
            #                    content_type='application/json')
    except ValidationError:
        return HttpResponse(status=400, content="Improper format.")


@login_required
def lendings(request):
    """List a users lendings. (For admins: List all lendings.)"""

    if request.user.is_superuser:
        lendings = Lending.objects.all()
    else:
        lendings = Lending.objects.get(user=request.user)

    return render(request, 'lendings.tmpl', locals())
