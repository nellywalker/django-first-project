from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Person
from .forms import PersonForm

def home(request):
    return render(request, 'home.html')

def person_list(request):
    persons = Person.objects.all()
    return render(request, 'person/list.html', {'persons': persons})

def person_create(request):
    form = PersonForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Personne ajoutée avec succès.")
        return redirect('person_list')
    return render(request, 'person/form.html', {'form': form, 'title': "Ajouter une personne"})

def person_update(request, pk):
    person = get_object_or_404(Person, pk=pk)
    form = PersonForm(request.POST or None, instance=person)
    if form.is_valid():
        form.save()
        messages.success(request, "Modifications enregistrées.")
        return redirect('person_list')
    return render(request, 'person/form.html', {'form': form, 'title': "Modifier la personne"})

def person_delete(request, pk):
    person = get_object_or_404(Person, pk=pk)
    if request.method == "POST":
        person.delete()
        messages.success(request, "Personne supprimée.")
        return redirect('person_list')
    return render(request, 'person/confirm_delete.html', {'person': person})
