from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

class Register(View):
    template_name = 'buzzytemplates/register.html'

    def get(self, request, *args, **kwargs):
        # Handle GET request
        context = {'Title': 'Welcome To the Buzzy ERP System'}

       

        return render(request, self.template_name, context)


class Login(View):
    template_name = 'buzzytemplates/login.html'

    def get(self, request, *args, **kwargs):
        context = {'Title': 'Welcome To the Buzzy ERP System'}

        return render(request, self.template_name, context)

