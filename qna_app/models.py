from django.db import models

# Create your models here.
class CategoryModel(models.Model):
    cat_title=models.CharField(max_length=255)
    cat_desc=models.TextField()
    #objects=object.models.manager()
     
    def __str__(self):
        return self.cat_title


class QuestionModel(models.Model):
    title = models.CharField(max_length=255)
    posted_by = models.CharField(max_length=120)
    timestamp= models.DateTimeField(auto_now_add=True)
    question_desc= models.TextField()
    ques_img=models.ImageField(upload_to="QuestionImg",blank=True,null=True)
    ques_votes=models.IntegerField(default=0)
    #objects=object.models.manager()
    
    ques_cat=models.ForeignKey(CategoryModel,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return(self.title)



class AnswerModel(models.Model):
    answer_by= models.CharField(max_length=255)
    timestamp= models.DateTimeField(auto_now_add=True)
    ans_desc= models.TextField()
    ans_img=models.ImageField(upload_to="AnswerImg",blank=True,null=True)
    ans_votes=models.IntegerField(default=0)
    isaccept=models.BooleanField(default=0)
    question= models.ForeignKey(QuestionModel,on_delete=models.CASCADE)
    #ans_cat=models.ForeignKey(CategoryModel,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return(self.answer_by)


    

