from django.forms import ModelForm
from main.models import Todo

class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ["name", "deadline", "description"]