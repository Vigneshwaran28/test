from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def students_view(request):
    obj = Student.objects.all()
    return render(request, 'index.html', {'obj': obj})


# @login_required()
def student_create_view(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            # task = form.save(commit=False)
            # task.user = request.user
            # task.save()
            form.save()
            return redirect('home')
        

    return render(request, 'students_create.html', {'form': form})


@login_required()
def student_delete_view(request, id):
    obj = Student.objects.get(id=id)
    obj.delete()

    return redirect('home')


@login_required()
def students_update_view(request, id):
    obj = Student.objects.get(id=id)
    form = StudentForm(instance=obj)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request, 'students_create.html', {'form': form})


def user_register_view(request):
    form = UserRegistrationForm()
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'registration.html', {'form': form})