from django.http import HttpResponseNotFound
from django.shortcuts import render

from .forms import StudentForm
from .models import Course, Student


# Create your views here.
def index(request):
    class_list = Course.objects.all()
    context = dict()
    print(class_list)
    context['classes'] = class_list
    context['sina'] = "sina"
    return render(request, 'faculty/index.html', context=context)


def detail(request, course_id):
    course = Course.objects.get(pk=course_id)
    if course:
        context = dict()
        context['course_data'] = course
        print(course)
        return render(request, 'faculty/detail.html', context=context)
    return HttpResponseNotFound('<h1> not found</h1>')


def register(request):
    studentform = StudentForm()
    if request.method == "POST":
        studentform = StudentForm(request.POST)
        if studentform.is_valid():
            studentform.save()
            return render(request, 'faculty/register.html', context={"save": True})
        return render(request, 'faculty/register.html', context={"save": False, "form": studentform})
    else:
        return render(request, 'faculty/register.html', context={"form": studentform})


def select_course(request):
    if request.method == 'POST':
        print(request.POST)
        student_id = request.POST["student"]
        cours_id = request.POST['cours']
        cours = Course.objects.get(id=cours_id)
        student=Student.objects.get(id=student_id)
        cours.students.add(student)
        cours.save()
        students = Student.objects.all()
        courses = Course.objects.all()
        return render(request, 'faculty/select.html', context={'save':True,"students": students, "courses": courses})
    else:
        students = Student.objects.all()
        courses = Course.objects.all()
        return render(request, 'faculty/select.html', context={"students": students, "courses": courses})
