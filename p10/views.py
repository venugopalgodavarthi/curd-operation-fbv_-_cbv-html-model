from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from app.models import book


def funcsample(request):
    if request.method=='POST':
        book.objects.create(name=request.POST['name'],author=request.POST['author'], publish=request.POST['publish'])
        return HttpResponse('data is inserted')
    return render(request,'func.html')

class clssample(View):
    def get(self,request):
        return render(request,'cls.html',)
    
    def post(self,request):
        if request.method=='POST':
            book.objects.create(name=request.POST['name'],author=request.POST['author'], publish=request.POST['publish'])
            return HttpResponse('data is inserted')
        
def funcselect(request):
    res=book.objects.all()
    return render(request,'fdetails.html',{'res':res})

class clsselect(View):
    def get(self,request):
        res=book.objects.all()
        return render(request,'cdetails.html',{'res':res})
    
    
def funcupdate(request,data):
    if request.method=='POST':
        book.objects.filter(id=data).update(name=request.POST['name'],author=request.POST['author'], publish=request.POST['publish'])
        return HttpResponse('data is update')
    res=book.objects.get(id=data)
    return render(request,'funcupdate.html',{'res':res})

class clsupdate(View):
    def get(self,request,data):
        res=book.objects.get(id=data)
        return render(request,'clsupdate.html',{'res':res})
    
    def post(self,request,data):
        if request.method=='POST':
            book.objects.filter(id=data).update(name=request.POST['name'],author=request.POST['author'], publish=request.POST['publish'])
            return HttpResponse('data is updated')
        
        
def funcdelete(request,data):
    book.objects.filter(id=data).delete()
    return HttpResponse('data is delete')

class clsdelete(View):
    def get(self,request,data):
        book.objects.filter(id=data).delete()
        return HttpResponse('data is delete')

'''
def funcsample(request):
    return HttpResponse('hello world function based view')

class clssample(View):
    def get(self,request):
        return HttpResponse('hello world class based view')
        

def funcsample(request):
    return render(request,'func.html')

class clssample(View):
    def get(self,request):
        return render(request,'cls.html')
        
def funcsample(request):
    data="welcome to pyspiders"
    return render(request,'func.html',{'data':data})

class clssample(View):
    def get(self,request):
        data="welcome to pyspiders"
        return render(request,'cls.html',{'data':data})
        
def funcsample(request,id):
    return render(request,'func.html',{'data':id})

class clssample(View):
    def get(self,request,id):
        return render(request,'cls.html',{'data':id})
        
        
def funcsample(request):
    book.objects.create(name='python',author='gudio',publish='python.org')
    return HttpResponse('value is insert')

class clssample(View):
    def get(self,request):
        book.objects.create(name='django',author='thmsom',publish='django.org')
        return HttpResponse('value is insert')
        
        
def funcsample(request):
    res=book.objects.all()
    return render(request,'details.html',{'res':res})

class clssample(View):
    def get(self,request):
        res=book.objects.all()
        return render(request,'details.html',{'res':res})
'''
    
