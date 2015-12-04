from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils.datastructures import MultiValueDictKeyError
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Category, Type, Lending
from datetime import datetime


def d(request_date):
    """Converts a date from a request in yyyy-mm-dd format to a datetime.date"""
    return datetime.strptime(request_date, "%Y-%m-%d").date()


def home(request):
    """List all available things. request has no parameters."""
    # TODO: Filtering, searching
    category_list = Category.objects.all()
    return render(request, 'things.tmpl', locals())


@login_required
def lend(request):
    """Try to lend a thing. request must contain thing id, startdate and enddate."""

    try: # extract and check request parameters
        type = Type.objects.get(id=request.GET['type'])
        startdate = d(request.GET['startdate_submit'])
        enddate = d(request.GET['enddate_submit'])
    except (ValueError, MultiValueDictKeyError):
        return HttpResponse(status=400, content="Insufficient data.")

    try:  # use model to lend thing
        things = type.available_things(startdate,enddate)
        if len(things) > 0 and things[0].lend(request.user, startdate, enddate, status="r"):
            messages.success(request, 'Ausleihvorgang erfolgreich. Das Gerät wurde reserviert. Bitte holen Sie es am %s ab.' % enddate)
            return redirect("lendings")
        else:
            messages.error(request, 'Das Gerät konnte nicht reserviert werden.')
            return redirect("home")
    except ValidationError:
        return HttpResponse(status=400, content="Improper format.")


@login_required
def lendings(request):
    """List a users lendings. (For admins: List all lendings.)"""

    def c(stat):
        return lendings.filter(status=stat).count()

    if request.user.is_superuser:
        lendings = Lending.objects.all()
    else:
        lendings = Lending.objects.filter(user=request.user)

    subviews = [{'status': 'l', 'title': 'Aktuell ausgeliehen',
                  'action': 'x', 'action_name': 'Rückgabe',
                  'cancel': request.user.is_superuser, 'num': c('l')},
                 {'status': 'r', 'title': 'Reserviert',
                  'action': 'l', 'action_name': 'Ausleihe', 'cancel': True, 'num': c('r')},
                 {'status': 'x', 'title': 'Zurückgegeben',
                  'action': None, 'cancel': False, 'num': c('x')},
                 {'status': 'o', 'title': 'Storniert','action': None,
                  'cancel': False, 'num': c('o')}]
    return render(request, 'lendings.tmpl', locals())


@login_required
def lending_status(request):
    """Changes the lending status of an object."""

    perm = False  # is operation allowed?
    try:  # extract and check request parameters
        lending = Lending.objects.get(id=request.GET['lending'])
        new_status = request.GET['new_status']
    except (ValueError, MultiValueDictKeyError):
        return HttpResponse(status=400, content="Insufficient data.")

    if not request.user.is_superuser:
        # non-superusers may only delete own reservations
        perm = (new_status == 'o' and lending.status == 'r' and lending.user == request.user)
    else:
        # superusers have superpowers
        perm = True

    if perm:
        if new_status in ['l', 'r', 'x', 'o']:
            lending.status = new_status
            lending.save()
            messages.success(request, 'Status erfolgreich geändert.')
            return redirect("lendings")
        else:
            messages.success(request, 'Ungültiger Status!')
            return redirect("lendings")
    else:
        messages.success(request, 'Das darfst du nicht.')
        return redirect("lendings")


@login_required
def settings(request):
    """Display and apply setting change page. request may be empty."""

    return render(request, "settings.tmpl")