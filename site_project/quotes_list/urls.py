from django.urls import path
from . import views

app_name = 'quotes_list'

urlpatterns = [
    path('', views.main, name='main'),
    path('create-author/', views.create_author, name='create_author'),
    path('create-quote/', views.create_quote, name='create_quote'),
    path('detail/<int:author_id>', views.author_details, name='author_details'),
    path('create-tag', views.tag, name = 'tag')

]