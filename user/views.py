from django.shortcuts import render
from django.views import View
from .models import Infomatsion, Service, Document


class Index(View):
    def get(self, request):
        try:    
            info = Infomatsion.objects.get(pk=1)    
            
        except:
            info == None
        service = Service.objects.all()
        documents = Document.objects.all()
        return render(request, 'index.html',
                      {'info': info,
                       'service': service,
                       'documents': documents}) 
