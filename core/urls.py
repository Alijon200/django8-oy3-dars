from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)




urlpatterns = [
    path('api/auth/login/', views.CunstomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("api/tests/<int:pk>/", views.TestUpdateDestroyView.as_view(), name="test-update-delete"),

    path('api/tests/<int:test_pk>/submission', views.SubmissonView.as_view(), name='submission-post'),
    path('api/submissions', views.SubmissionsListView.as_view(), name='submissions'),
    path('api/submissions/<int:pk>', views.SubmissionDetailView.as_view(), name='submissions-detail'),
    path('api/my-tests', views.MyTestListView.as_view(), name='my-test'),
    path('api/tests/<int:test_id>/questions', views.TestQuestionsListView.as_view(), name='questions'),
    path('api/questions/<int:pk>', views.TestQuestionDetailView.as_view(), name='question-detail'),
    path('api/my-submissions', views.MySubmissionListView.as_view(), name='my-submissions'),
    path("signup/", views.SignupCreatedView.as_view(), name="signup")
]
