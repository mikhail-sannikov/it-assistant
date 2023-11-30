from django.shortcuts import render
from django.views import View


class HomePage(View):
    def get(self, request):
        return render(request=request, template_name='core/homepage.html')


class InfoPage(View):
    def get(self, request):
        return render(request=request, template_name='core/infopage.html')
