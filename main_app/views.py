from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.contrib import messages

import requests

# Create your views here.
class Index(View):
    def get(self,request, *args, **kwargs):
        return render(request, 'index.html', {})

    def post(self,request, *args, **kwargs):
        print(request.POST)

        '''
        Required data for validate captcha
        captcha = the value of the captcha field
        secret = the secret key provided by reCAPTCHA
        ip = ip address site
        '''
        captcha = request.POST.get('g-recaptcha-response')
        secret = "6Lc4zxkUAAAAAN1kVE_UQG6ghpRTWLkfaMKphakq"
        ip = request.META.get('REMOTE_ADDR')
        validation_server = "https://www.google.com/recaptcha/api/siteverify"

        validation = requests.get(validation_server, params={'secret': secret, 'response':captcha,'remoteip':ip})
        response_validation = validation.json()
        print(response_validation)
        # if response_validation.get('success') : return HttpResponse("Approved")
        messages.success(request, "reCAPTCHA aproved :D") if response_validation.get('success') else messages.error(request, "reCAPTCHA error, it's a robot D: ")

        return redirect ('index')
