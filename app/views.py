from django.shortcuts import render, get_object_or_404, redirect
from .models import Todo_liste
from django import forms


class NoteForm(forms.ModelForm):
    class Meta:
        model = Todo_liste
        fields = ['designiation', 'contenu', 's_done']
        labels = {
            'designiation': 'Titre',
            'contenu': 'Contenu',
            's_done': 'Terminé',
        }
        widgets = {
            'designiation': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titre de la note'}),
            'contenu': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Contenu de la note', 'rows': 5}),
            's_done': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


def index(request):
    return render(request, "index.html")


def index2(request):
    return render(request, "index2.html")


def liste_notes(request):
    notes = Todo_liste.objects.all().order_by('-created')
    return render(request, "liste_notes.html", {'notes': notes})


def create_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = None  # pas d'utilisateur requis
            note.save()
            return redirect('app:listeNotes')
    else:
        form = NoteForm()
    return render(request, "create_note.html", {'form': form})


def update_note(request, pk):
    note = get_object_or_404(Todo_liste, pk=pk)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('app:listeNotes')
    else:
        form = NoteForm(instance=note)
    return render(request, "update_note.html", {'form': form, 'note': note})


def delete_note(request, pk):
    note = get_object_or_404(Todo_liste, pk=pk)
    if request.method == 'POST':
        note.delete()
        return redirect('app:listeNotes')
    return render(request, "delete_note.html", {'note': note})