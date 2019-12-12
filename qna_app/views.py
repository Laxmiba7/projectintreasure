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
    else:
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
    return render(request,'questionmodel_list.html',{'queslist':queslist})

def update_question(request,id):
    question= QuestionModel.objects.get(id=id)
    if request.method=="POST":
        form=QuestionForm(request.POST,request.FILES,instance=question) #request.files is for images
        if form.is_valid():
            try:
                form.save()
                return redirect('qna:update', id)
            except:
                return HttpResponse('Failed')
        else:
            return HttpResponse(form.errors)
    else:
        form= QuestionForm(instance=question)
    #question=QuestionModel.objects.all()
        return render(request,'questionmodel_update.html',{'form':form})



def del_question(request,id):
    question= QuestionModel.objects.get(id=id)
    question.delete()
    # return HttpResponse("deletequestionmodel_list.html")
    #question=QuestionModel.objects.all()
    return redirect('qna:queslist')