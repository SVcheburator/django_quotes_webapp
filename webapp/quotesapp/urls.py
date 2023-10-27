from django.urls import path
from . import views
from users import views as users_views

app_name = 'quotesapp'

urlpatterns = [
    path('', views.quotes_list, name='quotes_list'),
    path('tag/', views.tag, name='tag'),
    path('quote/', views.quote, name='quote'),
    path('author/', views.author, name='author'),
    path('authors_list/', views.authors_list, name='authors_list'),
    path('detail_q/<int:quote_id>', views.detail_q, name='detail_q'),
    path('detail_a/<int:quote_id>/<int:author_id>/', views.detail_a, name='detail_a'),
    path('delete_quote/<int:quote_id>', views.delete_quote, name='delete_quote'),
    path('delete_author/<int:author_id>', views.delete_author, name='delete_author'),
    path('accounts/login/', users_views.loginuser, name='login'),
    path('add_default_data/', views.add_default_data, name='add_default_data')
]