from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Course

courses = [
    {'code': 'TH001', 'name': 'Thai'},
    {'code': 'Eng002', 'name': 'English'},
    {'code': 'IR003', 'name': 'IR'},
]

def index(request):
    return render(request, 'myapp/index.html', {'courses': courses})

def search(request):
    result = None

    if request.method == 'POST':
        course_code = request.POST.get('course_code')
        result = next((course for course in courses if course['code'] == course_code), None)

    return render(request, 'myapp/search.html', {'result': result})

def search_by_name(request):
    result = None

    if request.method == 'POST':
        course_name = request.POST.get('course_name')
        result = next((course for course in courses if course['name'] == course_name), None)

    return render(request, 'myapp/search_by_name.html', {'result': result})

def edit_course(request, code):
    result = next((course for course in courses if course['code'] == code), None)

    if result is None:
        return redirect('index')

    if request.method == 'POST':
        result['name'] = request.POST.get('course_name')

        return redirect('index')

    return render(request, 'myapp/edit_course.html', {'result': result})

def delete_course(request, code):
    try:
        course = Course.objects.get(code=code)
    except Course.DoesNotExist:
        return redirect('index')

    if request.method == 'POST':
        course.delete()
        return redirect('index')

    return render(request, 'myapp/delete_course.html', {'result': course})

