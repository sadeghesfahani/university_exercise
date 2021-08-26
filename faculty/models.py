from django.db import models


# Create your models here.


class Staff(models.Model):
    first_name = models.CharField(max_length=250, blank=False, null=False)
    last_name = models.CharField(max_length=250, blank=False, null=False)
    staff_id = models.PositiveSmallIntegerField(blank=False, null=False, unique=True)
    TEACHER = 1
    EMPLOYEE = 2
    SECURITY = 3
    EXISTING_ROLLS = [
        (TEACHER, 'teacher'),
        (EMPLOYEE, 'employee'),
        (SECURITY, 'security')
    ]
    role = models.PositiveSmallIntegerField(choices=EXISTING_ROLLS)

    def __str__(self):
        return f"{self.first_name} - {self.last_name}"


class Faculty(models.Model):
    name = models.CharField(max_length=250)
    staff = models.ManyToManyField(Staff, blank=True, null=True)

    def __str__(self):
        return f"{self.name}"


class Student(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    student_id = models.PositiveSmallIntegerField(unique=True)
    faculty = models.ForeignKey(Faculty, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.first_name} - {self.last_name} - {self.student_id}"


class ClassRoom(models.Model):
    class_id = models.PositiveSmallIntegerField()
    capacity = models.PositiveSmallIntegerField()
    faculty = models.ForeignKey(Faculty, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.class_id} - {self.capacity} - {self.faculty.name}"


class Course(models.Model):
    name = models.CharField(max_length=250)
    capacity = models.PositiveSmallIntegerField()
    classes = models.ManyToManyField(ClassRoom)
    ACTIVE = True
    DEACTIVE = False
    EXISTING_STATUS = [
        (ACTIVE, "Active"),
        (DEACTIVE, "Deactive")
    ]
    students = models.ManyToManyField(Student, null=True, blank=True)
    status = models.BooleanField(choices=EXISTING_STATUS)
    # teacher = models.ForeignKey(Staff, on_delete=models.PROTECT,null=True)

    def __str__(self):
        return f"{self.name} - {self.capacity} - {self.status}"
    @property
    def getClasses(self):
        return self.classes.all()
        # return ", ".join([p.id for p in self.classes.all()])

