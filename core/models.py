from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()


class Test(models.Model):
    nomi = models.CharField(max_length=200)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)



class Question(models.Model):
    title = models.TextField()
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name="questions")
    created_at = models.DateTimeField(auto_now_add=True)



class Answers(models.Model):
    title = models.CharField()
    is_true = models.BooleanField(default=False)
    question = models.ForeignKey(Question, models.CASCADE, related_name="answers")
    created_at = models.DateTimeField(auto_now_add=True)


class Submission(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name="submissions")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class SelectedAnswer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.SET_NULL, null=True)
    answer = models.ForeignKey(Answers, on_delete=models.SET_NULL, null=True)
    submission = models.ForeignKey(Submission, on_delete=models.CASCADE, related_name="selected_answers")
    is_true = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    question_title = models.CharField(default="")
    answer_title = models.CharField(default="")
    correct_answer_title = models.CharField(default="")

