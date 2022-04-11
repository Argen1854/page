from django.urls import path
from . import views
urlpatterns = [
    path('api/v1/recordslist/', views.CreateListRecordsAPIView.as_view()),
    path('api/v1/<int:id>/', views.ListTimeRecordsAPIView.as_view()),
    path('api/v1/m/<int:id>/', views.ListFreeDayAPIView.as_view()),
    path('api/v1/user/records/<int:id>/', views.ListUserRecordsAPIView.as_view())
]
