from django.http import HttpResponse
from rest_framework import viewsets
from .models import Credential
from .serializers import CredentialSerializer

from django.shortcuts import render, redirect

class CredentialModelViewSet(viewsets.ModelViewSet):
    queryset = Credential.objects.all()
    serializer_class = CredentialSerializer

# Create your views here.


def create_credential(request):
    if request.method == "POST":
        name = request.POST.get("name")
        code = request.POST.get("code")

        if not name or not code:
            return HttpResponse("Both name and code are required", status=400)

        # Save to database
        Credential.objects.create(name=name, code=code)
        return HttpResponse("created successfully", status=201)  # Redirect after success

    return render(request, "create_credential.html")  # Render form template
