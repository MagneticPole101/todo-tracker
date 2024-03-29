from django.urls import path
from main.views import show_main, create_todo, show_xml, show_json, show_xml_by_id, show_json_by_id
from main.views import register, login_user, logout_user, edit_todo, delete_todo

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-todo', create_todo, name='create_todo'),    
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('edit-todo/<int:id>', edit_todo, name='edit_todo'),
    path('delete/<int:id>', delete_todo, name='delete_todo')
]