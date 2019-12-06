from django.shortcuts import render
from .models import Scholarship, Donor, Applicant, Parent
from django.template.response import TemplateResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import DonorForm, ApplicantForm, ParentForms
from rest_framework import viewsets

from ffutche.sterilizers import DonorSerlizer, ScholarshipSerializer, ApplicantSerializer, ParentSerializer


# # Create your views here.


def welcome(request):
    return render(request, 'Website.html')


def login(request):
    form = UserCreationForm()
    return render(request, 'Signin.html', {'form': form})


def register(request):
    return render(request, 'JoinUs.html')


def applicant(request):
    return render(request, 'applicant.html')


def parent(request):
    return render(request, 'parent.html')


def portal(request):
    return render(request, 'WebPortal.html')


def donor(request):
    return render(request, 'donor.html')


def scholarships(request):
    data = Scholarship.objects.all()
    return TemplateResponse(request, 'scholarships.html', {"data": data})

def donor_create_view(request):
    my_form = DonorForm(request.POST or None)
    if my_form.is_valid():
        my_form.save()
        my_form = DonorForm
    context = {
        'form': my_form
    }
    return render(request, 'donor.html', context)

def app_create_view(request):
    my_form = ApplicantForm(request.POST or None)
    if my_form.is_valid():
        my_form.save()
        my_form = ApplicantForm
    context = {
        'form': my_form
    }
    return render(request, 'applicant.html', context)

def parent_create_view(request):
    my_form = ParentForms(request.POST or None)
    if my_form.is_valid():
        my_form.save()
        my_form = ParentForms
    context = {
        'form': my_form
    }
    return render(request, 'parent.html', context)


class DonorView(viewsets.ModelViewSet):
    queryset = Donor.objects.all()
    serializer_class = DonorSerlizer

class ScholarshipView(viewsets.ModelViewSet):
    queryset = Scholarship.objects.all()
    serializer_class = ScholarshipSerializer

class ApplicantView(viewsets.ModelViewSet):
    queryset = Applicant.objects.all()
    serializer_class = ApplicantSerializer

class ParentView(viewsets.ModelViewSet):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer

