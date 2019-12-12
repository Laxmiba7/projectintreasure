from django.shortcuts import render,redirect
from .models import QuestionModel,AnswerModel,CategoryModel
from .forms import QuestionForm
from django.http import HttpResponse

# Create your views here.
def addquestion(request):
    if request.method=="POST":
        form=QuestionForm(request.POST,request.FILES) #request.files is for images
        if form.is_valid():
            try:
                form.save()
                return HttpResponse('Submitted')
            except:
                return HttpResponse('Failed')
        else:
            return HttpResponse(form.errors)
    form= QuestionForm
    #question=QuestionModel.objects.all()
    return render(request,'questionmodel_create.html',{'d':form})

def popques(request):
    pop=QuestionModel.objects.filter(ques_votes__gt=2)
    return render(request,'popques.html',{'p':pop})

def question(request):
    ques=QuestionModel.objects.all()
    return render(request,'question.html',{'q':ques})

def queslist(request):
    queslist=QuestionModel.objects.all()
    return render(request,'questionmodel_list',{'list':queslist})
