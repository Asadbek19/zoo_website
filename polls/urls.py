from django.urls import path

from .views import (
    index,
    zoo,
    info,
    tickets,
    events,
    gallery,
    contact,
    blog,
    live
    # detail
)

# urlpatterns = [
#     path("", index, name='index'),
#     path('<str:question_id>/', detail, name='detail')
#
# ]

urlpatterns = [
    path("", index, name='index'),
    path('zoo/', zoo, name='zoo'),
    path('info/', info, name='info'),
    path('tickets/', tickets, name='tickets'),
    path('events/', events, name='events'),
    path('gallery/', gallery, name='gallery'),
    path('contact/', contact, name='contact'),
    path('blog/', blog, name='blog'),
    path('live/', live, name='live')
]

