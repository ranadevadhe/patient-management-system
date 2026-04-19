from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .models import Patient, Appointment
from .forms import PatientForm, AppointmentForm

def login_view(request):
    form = AuthenticationForm(data=request.POST or None)
    if form.is_valid():
        user = form.get_user()
        login(request, user)
        return redirect('dashboard')
    return render(request, 'login.html', {'form': form})


@login_required
def dashboard(request):
    return render(request, 'dashboard.html', {
        'patients': Patient.objects.count(),
        'appointments': Appointment.objects.count()
    })


@login_required
def patients(request):
    query = request.GET.get('q')
    data = Patient.objects.all()

    if query:
        data = data.filter(name__icontains=query)

    return render(request, 'patients.html', {'patients': data})


@login_required
def add_patient(request):
    form = PatientForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('patients')
    return render(request, 'add_patient.html', {'form': form})


@login_required
def appointments(request):
    data = Appointment.objects.all()
    return render(request, 'appointments.html', {'appointments': data})


@login_required
def add_appointment(request):
    form = AppointmentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('appointments')
    return render(request, 'add_patient.html', {'form': form})

def add_doctor(request):
    from .forms import DoctorForm
    form = DoctorForm()

    if request.method == "POST":
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/dashboard/')

    return render(request, 'add_doctor.html', {'form': form})