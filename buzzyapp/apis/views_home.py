from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

class Home(View):
    template_name = 'buzzytemplates/home.html'

    def get(self, request, *args, **kwargs):
        # Handle GET request
        context = {'Title': 'Welcome To the Buzzy ERP System'}

        if request.user.is_authenticated:
            print("no bhaiya nhi h ")
        else:
            print("ha bhaiya h ")
            return render(request, 'buzzytemplates/login.html',context)
        return render(request, self.template_name, context)

