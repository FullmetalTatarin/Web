from django.urls import path
from Main.views import *
from Auth.views import *

urlpatterns = [
    path('', main_page, name='main-page'),
    path('addBook/', add_book, name='add-book'),
    path('changeBook/<int:id>/', change_book, name='change-book'),
    path('deleteBook/<int:id>/', delete_book, name='delete-book'),
    path('reg', reg_user, name='reg-user'),
    path('login', login, name='login'),
    path('logout', logout, name='logout'),
    path('validate_login', validate_login, name='validate_login'),
    path('validate_email', validate_email, name='validate_email')
]
