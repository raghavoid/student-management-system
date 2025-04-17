from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from student.models import Notification, Student, Parent

# Create your views here.

def index(request):
    return render(request, "authentication/login.html")

def dashboard(request):
    students = Student.objects.all()  # Retrieve all students
    unread_notification = Notification.objects.filter(user=request.user, is_read=False)
    unread_notification_count = unread_notification.count()
    return render(request, "students/student-dashboard.html", {
        "students": students,
        "unread_notification_count": unread_notification_count,
    })

def mark_notification_as_read(request):
    if request.method == 'POST':
        notification = Notification.objects.filter(user=request.user, is_read=False)
        notification.update(is_read=True)
        return JsonResponse({'status': 'success'})
    return HttpResponseForbidden()

def clear_all_notification(request):
    if request.method == "POST":
        notification = Notification.objects.filter(user=request.user)
        notification.delete()
        return JsonResponse({'status': 'success'})
    return HttpResponseForbidden