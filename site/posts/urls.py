from django.urls import path
from . import views
urlpatterns = [
    path('',views.PostPageView.as_view(),name='posts'),
    path('new/',views.NewPostPageView.as_view(),name='new_post'),
]
