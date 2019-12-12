from django.urls import path
#from .views import addquestion,popques,question,update_question
from qna_app import views

app_name='qna'

urlpatterns=[
    path('addquestion/',views.addquestion,name='add'),
    path('popques/',views.popques,name='popularques'),
    path('question/',views.question,name='question'),
    path('update/<int:id>/',views.update_question,name='update'),
    path('queslist',views.queslist,name='queslist'),
    path('del_ques/<int:id>/',views.del_question,name='del'),
]
