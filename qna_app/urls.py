from django.urls import path
#from .views import addquestion,popques,question,update_question
from qna_app import views
# from django.views.generic import QuestionModelCreateView


app_name='qna'

urlpatterns=[
    path('addquestion/',views.addquestion,name='add'),
    path('popques/',views.popques,name='popularques'),
    path('question/',views.question,name='question'),
    path('update/<int:id>/',views.update_question,name='update'),
    path('queslist',views.queslist,name='queslist'),
    path('del_ques/<int:id>/',views.del_question,name='del'),
    path('quesmodel/',views.QuestionModelCreateView.as_view(),name='quesmodel'),
    path('listmodel/',views.QuestionModelListView.as_view(),name='listmodel')
]
