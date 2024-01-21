from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *
from .forms import *


def start(request):
    return render(request, "home.html")


def add_teacher(request):
    if request.method == "POST":
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list_teachers")
    else:
        form = TeacherForm()
    return render(request, "add_teacher.html", {"form": form})


def list_teachers(request):
    teachers = Teacher.objects.all()
    return render(request, "list_teachers.html", {"teachers": teachers})


def add_group(request):
    if request.method == "POST":
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list_groups")
    else:
        form = GroupForm()
    return render(request, "add_group.html", {"form": form})


def list_groups(request):
    groups = Group.objects.all()
    return render(request, "list_groups.html", {"groups": groups})


def add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list_students")
    else:
        form = StudentForm()
    return render(request, "add_student.html", {"form": form})


def list_students(request):
    students = Student.objects.all()
    return render(request, "list_students.html", {"students": students})


def edit_teacher(request, pk):
    teacher = Teacher.objects.get(pk=pk)
    if request.method == "GET":
        form = TeacherForm(instance=teacher)
        return render(request, "edit_teacher.html", {"form": form})
    form = TeacherForm(request.POST, instance=teacher)
    if form.is_valid() and "ok" in request.POST:
        form.save()
        return redirect("list_teachers")
    if "delete" in request.POST:
        groups = teacher.group.all()
        if not groups:
            teacher.delete()
            return redirect("list_teachers")
        return HttpResponse("<h3>This teacher has groups and cannot be deleted<м/h3>")
    return render(request, "edit_teacher.html", {"form": form})


# def edit_group(request):


def edit_student(request, pk):
    student = Student.objects.get(pk=pk)
    if request.method == "GET":
        form = StudentForm(instance=student)
        return render(request, "edit_student.html", {"form": form})
    form = StudentForm(request.POST, instance=student)
    if form.is_valid() and "ok" in request.POST:
        form.save()
        return redirect("list_students")
    if "delete" in request.POST:
        student.delete()
        return redirect("list_students")
    return render(request, "edit_student.html", {"form": form})
