from django.urls import path


from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:pk>', views.postDetail, name='post-details'),
    path('post/<slug:slug>', views.postDetailWithSlug, name='post-details'),

]