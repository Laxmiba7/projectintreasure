from django.db import models

# Create your models here.
class QuestionModel(models.Model):
    title = models.CharField(max_length=255)
    posted_by = models.CharField(max_length=120)
    timestamp= models.DateTimeField(auto_now_add=True)
    question_desc= models.TextField()
    ques_img=models.ImageField(upload_to="QuestionImg")


class AnswerModel(models.Model):
    answer_by= models.CharField(max_length=255)
    timestamp= models.DateTimeField(auto_now_add=True)
    ans_desc= models.TextField()
    ans_img=models.ImageField(upload_to="AnswerImg")
    votes=models.IntegerField()
    isaccept=models.BooleanField()
    question= models.ForeignKey(QuestionModel,on_delete=models.CASCADE)
    