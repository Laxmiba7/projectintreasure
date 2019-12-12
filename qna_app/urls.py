from django.urls import path
from .views import addquestion,popques,question

urlpatterns=[
    path('addquestion/',addquestion),
    path('popques/',popques),
    path('question/',question),
]
