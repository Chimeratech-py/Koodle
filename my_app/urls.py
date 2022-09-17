from django.urls import path
from . import views

urlpatterns = [
    path('<int:num_page>',views.topic_view),
    path('<topic>',views.articles_view,name='topic-view')
    #path('<int:num1>/<int:num2>',views.experiment_view)
]