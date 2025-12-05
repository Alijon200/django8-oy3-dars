from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .serializer import TestSerializer, QuestionSerializer, SubmissionSerializer, CustomTokenObtainPairSerializer, MyTestSerializer, MySubmissionSerializer, SubmissionFULLSerializer
from .models import Test, Question, Submission
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView, ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView 
from rest_framework import status
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from rest_framework.exceptions import NotFound
# Create your views here.




class TestUpdateDestroyView(DestroyAPIView, UpdateAPIView):
    serializer_class = TestSerializer
    queryset = Test.objects.all()
    permission_class = [IsAuthenticated]



# class QuestionCreateAPIView(CreateAPIView):   
#     serializer_class = QuestionSerializer
#     permission_classes = [IsAuthenticated]

#     def perform_create(self, serializer):
#         test = Test.objects.get(pk=self.kwargs['test_pk'])
#         serializer.save(test=test)
    

class SubmissonView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = SubmissionSerializer

    def perform_create(self, serializer):
        test = Test.objects.get(pk=self.kwargs['test_pk'])
        serializer.save(test=test, user = self.request.user)
    


class SubmissionsListView(ListAPIView):
    serializer_class = SubmissionSerializer
    permission_classes = [IsAuthenticated]
    queryset = Submission.objects.all()
    


class CunstomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class MyTestListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = MyTestSerializer
    
    def get_queryset(self):
        return Test.objects.filter(creator=self.request.user)


class TestQuestionsListView(ListCreateAPIView):
    serializer_class = QuestionSerializer


    def get_test(self):
        try:
            test = Test.objects.get(pk = self.kwargs["test_id"])
            return test
        except Test.DoesNotExist:
            raise NotFound(detail="Test not found")
        

    def get_queryset(self):
        test = self.get_test()
        return Question.objects.filter(test = test)

    
    def perform_create(self, serializer):
        test = self.get_test()
        serializer.save(test = test)

    
class TestQuestionDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    


class MySubmissionListView(ListAPIView):
    serializer_class = MySubmissionSerializer
    permission_classes = [IsAuthenticated]


    def get_queryset(self):
        return Submission.objects.filter(user = self.request.user)


class SubmissionDetailView(RetrieveAPIView):
    serializer_class = SubmissionFULLSerializer
    queryset = Submission.objects.all()