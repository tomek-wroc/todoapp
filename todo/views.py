from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# from django.views.generic.detail import DetailView
# from django.http import HttpResponseForbidden

from .models import Task, TASKS_STATUS  # , LocationChoices
from .forms import TaskForm
from weatherMapApi.utils import fetchWeather, fetchWeatherLatLon,  calcBackgroundColor

import requests

DEFAULT_BACKGROUND_COLOR = '#FFFFFF'  # Default color (white) #FFFFFF


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
        # Get the current logged-in user
        user = self.request.user
        # Filter tasks by the current user (sql query with WHERE statement is executed under the hood)
        queryset = Task.objects.filter(user=user)
        # in loop
        for task in queryset:
            try:
                # Omit calculation when location is empty
                if task.location == None:
                    task.background_color = DEFAULT_BACKGROUND_COLOR
                    task.status = statuses_dict[task.status]
                # Calculate value for not finished task only
                elif task.status != 2:
                    # Change the code to meaning for people
                    task.status = statuses_dict[task.status]
                    # Use calculation from cache if exists
                    if task.location == 'Current_Loc' and task.location in dictionary_locations:
                        task.background_color = dictionary_locations[task.location]
                    else:
                        # Check weather related to location
                        if task.location == 'Current_Loc':
                            response = fetchWeatherLatLon(
                                task.latitude, task.longitude)
                        else:
                            response = fetchWeather(task.location)
                        # Parsing response
                        json_response = response.json()
                        # Set weather and temperature in celsius degress of selected location
                        task.weather = json_response['weather'][0]['main']
                        task.temp = json_response['main']['temp']
                        # Calculate background color
                        task.background_color = calcBackgroundColor(
                            task.weather, task.temp)
                        # Add calculation to temporary cache
                        dictionary_locations[task.location] = task.background_color
                # Use last values before finished task to calculate background color
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
        # form = custom_valid(self, form)
        return super().form_valid(form)


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    context_object_name = 'task'

    template_name = 'todo/task_update_form.html'
    success_url = reverse_lazy('tasks_list')

    # Method is called when the form is valid, and it's where you can customize what happens when a new task is created
    def form_valid(self, form):
        original_instance = self.get_object()
        if original_instance.status == 2:
            # form = custom_valid(self, form)
            # else:
            form.add_error(
                'status', 'The task has been completed (Staus = Done) and cannot be changed.')
            return super().form_invalid(form)
        return super().form_valid(form)


class DeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    # Custom object name in template
    context_object_name = 'task'
    success_url = reverse_lazy('tasks_list')


