from django.shortcuts import render
from .models import Departament,Seminari
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
class MantenimentFormulari(LoginRequiredMixin, generic.ListView):
    template_name = "batx_seminaris/manteniment_formulari.html"
    context_object_name = "llista_manteniment"
    departaments = Departament.objects.all()
    seminaris = Seminari.objects.all().values()
    for departament in departaments:
        departament[0].seminariss= seminaris[0]

        print(departament.nom,departament.id )
