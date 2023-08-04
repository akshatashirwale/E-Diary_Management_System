
from django.contrib import admin
from django.urls import path
from eDiary.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('registration', registration, name='registration'),
    path('user_login', user_login, name='user_login'),
    path('user_home', user_home, name='user_home'),
    path('manageCategory', manageCategory, name='manageCategory'),
    path('editCategory/<int:pid>', editCategory, name='editCategory'),
    path('deleteCategory/<int:pid>', deleteCategory, name='deleteCategory'),
    path('manageNotes', manageNotes, name='manageNotes'),
    path('editNotes/<int:pid>', editNotes, name='editNotes'),
    path('viewNotes/<int:pid>', viewNotes, name='viewNotes'),
    path('deleteNotesHistory/<int:pid>', deleteNotesHistory, name='deleteNotesHistory'),
    path('deleteNotes/<int:pid>', deleteNotes, name='deleteNotes'),
    path('searchNotes', searchNotes, name='searchNotes'),
    path('profile', profile, name='profile'),
    path('changePassword', changePassword, name='changePassword'),
    path('logout/', Logout, name='logout'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
