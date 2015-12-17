from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.utils.datastructures import MultiValueDictKeyError
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.translation import ugettext as _
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


def type(request, type_id):
    """Show details for one type and display lending form."""
    type=get_object_or_404(Type, pk=type_id)
    num_things = type.thing_set.count()
    return render(request, 'type.tmpl', locals())


def about(request):
    """Show about page."""
    return render(request, 'about.tmpl', locals())


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
            messages.success(request, _('Ausleihvorgang erfolgreich. Das Gerät wurde reserviert. Bitte holen Sie es am %s ab.') % enddate)
            return redirect("lendings")
        else:
            messages.error(request, _('Das Gerät konnte nicht reserviert werden.'))
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

    subviews = [{'status': 'l', 'title': _('Aktuell ausgeliehen'),
                  'action': 'x', 'action_name': _('Rückgabe'),
                  'cancel': request.user.is_superuser, 'num': c('l')},
                 {'status': 'r', 'title': _('Reserviert'),
                  'action': 'l', 'action_name': _('Ausleihe'), 'cancel': True, 'num': c('r')},
                 {'status': 'x', 'title': _('Zurückgegeben'),
                  'action': None, 'cancel': False, 'num': c('x')},
                 {'status': 'o', 'title': _('Storniert'),'action': None,
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
            messages.success(request, _('Status erfolgreich geändert.'))
            return redirect("lendings")
        else:
            messages.success(request, _('Ungültiger Status!'))
            return redirect("lendings")
    else:
        messages.success(request, _('Das darfst du nicht.'))
        return redirect("lendings")


@login_required
def settings(request):
    """Display and apply setting change page. request may be empty."""

    return render(request, "settings.tmpl", {'request':request})