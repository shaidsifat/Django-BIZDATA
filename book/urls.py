 


from django.urls import path,include
from . import views
from book.views import BookList
urlpatterns = [
    
    path('csv',views.getfile),
    path('data',BookList.as_view(),name='book')
]

