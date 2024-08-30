from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView , DetailView , UpdateView , DeleteView , ListView
from django.urls import reverse_lazy


from .models import Trip,Note

# Create your views here.
class HomeView(TemplateView):
    template_name = 'triptrak/index.html'

def trips_list(request):
    if not request.user.is_authenticated:
        return HttpResponse('Go & Login')

    trips = Trip.objects.filter(owner=request.user)

    context = {
        'trips': trips
    }

    return render(request,'triptrak/trips_list.html',context)


class TripCreateView(CreateView):
    model = Trip
    success_url = reverse_lazy('trip-list')
    fields = ['city','country','start_date','end_date']
    # This view will be looking for a template Model_form.html

    # overriding a function 
    def form_valid(self, form):
        #owner from Trip Model should be logged in user when the form gets submitted.
        form.instance.owner = self.request.user
        return super().form_valid(form)
    
class TripDetailView(DetailView):
    model = Trip
    # we would get the data stored on trip Model & also have the Notes Data

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        trip = context['object']
        notes = trip.notes.all() #Note model has trip which is a foreignKey to Trip Model & it's name is notes -> gives us notes associated with that trip.
        context['notes'] = notes

        return context

class NoteDetailView(DetailView):
    model = Note

class TripUpdateView(UpdateView):
    model = Trip
    success_url = reverse_lazy('trip-list')
    fields = ["city", "country", "start_date", "end_date"]
    #template named model_form.html

class TripDeleteView(DeleteView):
    model = Trip
    success_url = reverse_lazy('trip-list')

class NoteListView(ListView):
    model = Note

    def get_queryset(self):
        queryset = Note.objects.filter(trip__owner=self.request.user)
        return queryset

class NoteDetailView(DetailView):
    model = Note

class NoteCreateView(CreateView):
    model = Note
    success_url = reverse_lazy('note-list')
    fields = "__all__"

    def get_form(self):
        form = super(NoteCreateView, self).get_form()
        trips = Trip.objects.filter(owner=self.request.user)
        form.fields['trip'].queryset = trips
        return form

class NoteUpdateView(UpdateView):
    model = Note
    success_url = reverse_lazy('note-list')
    fields = "__all__"

    def get_form(self):
        form = super(NoteUpdateView, self).get_form()
        trips = Trip.objects.filter(owner=self.request.user)
        form.fields['trip'].queryset = trips
        return form

class NoteDeleteView(DeleteView):
    model = Note
    success_url = reverse_lazy('note-list')
    #not make the template - send post requests here