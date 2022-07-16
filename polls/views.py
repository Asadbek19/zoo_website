from django.shortcuts import render
from django.http import HttpResponse
from .models import Event

# def index(request):
#     return HttpResponse("Some text")


# def detail(request, question_id):
#     return HttpResponse(f"Ваш проект какой-то какой-то {question_id}")

#
# def results(request, question_id):
#     response = f"You're looking at the results of question {question_id}"

def index(request):
    event = Event.objects.all()
    context = {
        'title': 'In the Zoo',
        'selected_home': 'selected',
        'event': event
    }
    return render(request, 'polls/index.html', context=context)


def zoo(request):
    context = {
        'title': 'The  Zoo',
        'selected_zoo': 'selected'
    }
    return render(request, 'polls/zoo.html', context=context)


def info(request):
    context = {
        'title': 'Visitors Info',
        'selected_info': 'selected'
    }
    return render(request, 'polls/info.html', context=context)


def tickets(request):
    context = {
        'title': 'Tickets',
        'selected_tickets': 'selected'
    }
    return render(request, 'polls/tickets.html', context=context)


def events(request):
    context = {
        'title': 'Events',
        'selected_events': 'selected'
    }
    return render(request, 'polls/events.html', context=context)


def gallery(request):
    context = {
        'title': 'Gallery',
        'selected_gallery': 'selected'
    }
    return render(request, 'polls/gallery.html', context=context)


def contact(request):
    context = {
        'title': 'Contacts',
        'selected_contact': 'selected'
    }
    return render(request, 'polls/contact.html', context=context)


def blog(request):
    context = {
        'title': 'Blog',
        'selected_blog': 'selected'
    }
    return render(request, 'polls/blog.html', context=context)


def live(request):
    context = {
        'title': 'Live',
        'selected_live': 'selected'
    }
    return render(request, 'polls/live.html', context=context)
