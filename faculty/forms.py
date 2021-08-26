from django.forms import forms, formset_factory, ModelForm
from .models import Student


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

