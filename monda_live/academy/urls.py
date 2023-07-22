from django.urls import path
from . import views

urlpatterns = [
    path('courses/', views.CourseListView.as_view(), name='course_list'),
    path('course/<slug:course_code>/', views.CourseTopicListView.as_view(), name='course_code'),
]
