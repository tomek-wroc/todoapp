from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.http import HttpResponseForbidden


from .models import Task, TASKS_STATUS, LocationChoices
from weatherMapApi.utils import fetchWeather, fetchWeatherLatLon,  calcBackgroundColor

import requests

DEFAULT_BACKGROUND_COLOR = '#BBBBBB'  # Default color (white) #FFFFFF


def dashboard(request):
    return render(request, "todo/welcome.html")


def default_if_none(value, default_value):
    return value if value is not None or value == '' else default_value


class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks_list'
    template_name = 'todo/tasks_list.html'

    def get_queryset(self):
        dictionary_locations = {}
        statuses_dict = dict(TASKS_STATUS)
        # location_dict = dict(LocationChoices)
        # Get the current logged-in user
        user = self.request.user
        # Filter tasks by the current user (sql query with WHERE statement is executed under the hood)
        queryset = Task.objects.filter(user=user)
        # in loop
        for task in queryset:
            try:
                if task.status != 2:
                    task.status = statuses_dict[task.status]
                    if task.location != 'Current_Loc' and task.location in dictionary_locations:
                        task.background_color = dictionary_locations[task.location]
                    else:
                        if task.location == 'Current_Loc':
                            response = fetchWeatherLatLon(task.latitude, task.longitude)
                        else:
                            response = fetchWeather(task.location)
                        
                        json_response = response.json()
                        task.weather = json_response['weather'][0]['main']
                        # Temperature in celsius degress of selected location
                        task.temp = json_response['main']['temp']
                        task.background_color = calcBackgroundColor(
                            task.weather, task.temp)
                        dictionary_locations[task.location] = task.background_color
                else:
                    task.status = statuses_dict[task.status]
                    task.background_color = calcBackgroundColor(
                            task.weather, task.temp)
            except requests.HTTPError as e:
                task.background_color = DEFAULT_BACKGROUND_COLOR
            except Exception as e:
                task.background_color = DEFAULT_BACKGROUND_COLOR
        return queryset


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    context_object_name = 'task'
    template_name = 'todo/task_create_form.html'
    fields = ['note', 'status', 'location']
    # Redirect to tasks list when task created correctly
    success_url = reverse_lazy('tasks_list')

    # Method is called when the form is valid, and it's where you can customize what happens when a new task is created
    def form_valid(self, form):
        # Set the user of the task to the currently logged-in user
        form.instance.user = self.request.user
        return super().form_valid(form)


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    context_object_name = 'task'
    fields = ['note', 'status', 'location']

    template_name = 'todo/task_update_form.html'
    success_url = reverse_lazy('tasks_list')

    # Method is called when the form is valid, and it's where you can customize what happens when a new task is created
    def form_valid(self, form):
        post_data = self.request.POST
        if post_data.get('latitude') != '':
            form.instance.latitude = post_data.get('latitude')
        if post_data.get('longitude') != '':
            form.instance.longitude = post_data.get('longitude')
        form.instance.weather = post_data.get('weather')
        if post_data.get('temp') != '' or post_data.get('temp') is not None :
            form.instance.temp = post_data.get('temp')
        if post_data.get('location') != 'Current_Loc':
            form.instance.latitude = None
            form.instancelongitude = None
        return super().form_valid(form)


class DeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    # Custom object name in template
    context_object_name = 'task'
    success_url = reverse_lazy('tasks_list')
