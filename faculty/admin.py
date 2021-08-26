from django.contrib import admin
from .models import Staff, Student, ClassRoom, Faculty, Course


# Register your models here.
class ClassRoomInline(admin.TabularInline):
    model = Course.classes.through


class StaffInline(admin.TabularInline):
    model = Faculty.staff.through


class StaffAdmin(admin.ModelAdmin):
    pass
    # inlines = [
    #     StaffInline,
    # ]


class FacultyAdmin(admin.ModelAdmin):
    inlines = [
        StaffInline
    ]
    list_filter = ['staff']


@admin.action(description='change class status')
def change_status(modeladmin, request, queryset):
    # queryset.update(status= not Course.status)
    for obj2 in queryset:
        obj2.status = not obj2.status
        obj2.save()

class CourseAdmin(admin.ModelAdmin):
    actions = [change_status]
    inlines = [ClassRoomInline]
    list_display = ["name","capacity","status"]



admin.site.register(Staff, StaffAdmin)
admin.site.register(Faculty, FacultyAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(ClassRoom)
admin.site.register(Student)