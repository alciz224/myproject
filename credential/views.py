from django.http import HttpResponse, HttpResponseRedirect
from django.http.request import urlencode
from rest_framework import viewsets
from .models import Credential
from .serializers import CredentialSerializer
from django.shortcuts import render, redirect, reverse

class CredentialModelViewSet(viewsets.ModelViewSet):
    queryset = Credential.objects.all()
    serializer_class = CredentialSerializer

# Create your views here.

def create_link(request):
    if request.method == "POST":

        link = request.POST.get("link")

        if not link:
            return HttpResponse("Invalid link", status=400)
        full_link=f"{request.build_absolute_uri(credential_link)}?{urlencode(params)}"
        return HttpResponseRedirect(full_link)
    return render(request, "create_link.html")


def create_credential(request):
    if request.method == "POST":
        name = request.POST.get("name")
        code = request.POST.get("code")

        if not name or not code:
            return HttpResponse("Both name and codee", status=400)

        # Save to database
        Credential.objects.create(name=name, code=code)
        return HttpResponse("valider")

    return render(request, "create_credential.html")  # Render form template
