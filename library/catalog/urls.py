from django.urls import path
from . import views
from .views import BookCreateView, BookDetailView, SignUpView, CheckedOutBooks

app_name = 'catalog'

urlpatterns = [
    path('', views.index, name='index'),
    path('create_book/', BookCreateView.as_view(), name='book_create'),
    path('book_detail/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('my_view/', views.my_view, name='my_view'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/', CheckedOutBooks.as_view(), name='profile')
]
