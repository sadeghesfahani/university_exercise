from django.urls import path

from faculty.views import index, detail, register, select_course

urlpatterns = [
    path('', index, name="index"),
    path('detail/<int:course_id>', detail, name='detail'),
    path('register', register, name="register"),
    path('select', select_course, name='select')
]
