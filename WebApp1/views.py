from django.shortcuts import render
from django.views import generic
from .models import Person
from django import forms
from django.core import validators
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from notify.signals import notify
from django.views.generic import View
import requests
import json

# Create your views here.

#
# def index(request):
#     strr = request.POST['dim']
#     notify.send(request.user, verb='test notification')
#     return render(request, 'WebApp1/index.html')


class IndexView(View):
    template_name = 'WebApp1/index.html'

    def get(self, request):
        return HttpResponse(200)

    def post(self, request):
        data = request.body.decode('utf-8').split(',')

        self.sendHttp(data)
        return HttpResponse(200)

    def sendHttp(self, data):
        url = "https://faultdetector.herokuapp.com/aibased/fault"
        j_data = {}

        j_data['location'] = data[0]
        j_data['v1'] = float(data[1])
        j_data['v2'] = float(data[2])
        j_data['v3'] = float(data[3])
        j_data['i1'] = float(data[4])
        j_data['i2'] = float(data[5])
        j_data['i3'] = float(data[6])

        json_data = json.dumps(j_data)
        print(json_data)

        payload = json_data
        headers = {
            'content-type': "application/json",
            'x-csrftoken': "6wmO5AJmovlQFNZobBGMKcAzUGPZDorNvpevQ4qDfIabBXXd4z17fsm0uqjHcVQT",
            'referer': "https://faultdetector.herokuapp.com",
            'authorization': "Basic cm9vdDpzbGFzaGhvc3Q=",
            'cache-control': "no-cache",
            'postman-token': "20b36330-cea2-c3fd-a9b4-cbb9789ad4b9"
        }

        response = requests.request("POST", url, data=payload, headers=headers)

        print(response.text)

# class Fault(View):
#     model = Person
#     template_name = 'WebApp1/detail.html'
#
#     def get(self, request):
#         return HttpResponse("Success Get Request")
#
#     def post(self, request):
#         return HttpResponse("Success post requset")
#
#
# class NoModel(forms.Form):
#
#     def no_model(request):
#         return HttpResponse('<h3>hello Django</h3>')
#
#     def clean(self):
#         cleaned_data = super(NoModel, self).clean()
#         name = cleaned_data.get('name')
#         pwd = cleaned_data.get('password')
#         print(name)
#     template_name = 'WebApp1/no_model.html'
