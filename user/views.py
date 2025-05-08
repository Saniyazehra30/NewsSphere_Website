from django.shortcuts import render
from .models import *
from django.http import HttpResponse
# Create your views here.
def index(request):
    data = Category.objects.all().order_by('-id')[:12]
    ndata = News.objects.all().order_by('-id')[0:8]
    cdata = city_news.objects.all().order_by('-id')[0:5]
    ndata2 = News.objects.all().order_by('-id')[0:3]
    sdata = slider.objects.all().order_by('-id')[0:3]
    context ={
        'newsdata': ndata,
        'cat_data': data,
        'city_data' : cdata,
        'ndata2' : ndata2,
        'sdata' : sdata,
    }
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def contact(request):
    mydict = {}
    if request.method == "POST":
        Name = request.POST.get('name')
        Email = request.POST.get('email')
        Mobile = request.POST.get('mobile')
        Msg = request.POST.get('msg')
        # mydict = {"name": Name,
        #           "email": Email,
        #           "mobile": Mobile,
        #           "message": Message}
        contactus(Name=Name,Email=Email,Mobile=Mobile,Message=Msg).save()
        return HttpResponse("<script>alert('Data Saved');location.href='/contact/'</script>")
    return render(request, 'contact.html')

def faqs(request):
    return render(request, 'faqs.html')

def job_news(request):
    jdata = Jobs.objects.all().order_by('-id')
    context = {
        'jobsdata': jdata,
    }
    return render(request, 'job_news.html', context)

def news(request):
    catid = request.GET.get('cid')
    cityid = request.GET.get('ctid')
    if catid is not None:
          data = News.objects.all().filter(news_category=catid).order_by('-id')
    elif cityid is not None:
          data = News.objects.all().filter(news_city=cityid).order_by('-id')
    else:
        data = News.objects.all().order_by('-id')

    citydata = city_news.objects.all().order_by('-id')
    catdata = Category.objects.all().order_by('-id')

    context = {
        'ndata': data,
        'citydata': citydata,
        'catdata': catdata,
    }
    return render(request, 'news.html' , context)

def video_news(request):
    return render(request, 'video_news.html')

def newsdetail(request):
    x=request.GET.get('nid')
    c =request.GET.get('idc')
    cat =request.GET.get('idcat')
    if x is not None :
         data = News.objects.all().filter(id=x).order_by('-id')
    elif c is not None :
         data = News.objects.all().filter(news_city = c).order_by('-id')
    elif cat is not None :
         data = News.objects.all().filter(news_category = cat).order_by('-id')
    context={
        'nd_data' : data,
    }
    return render(request , 'newsdetail.html', context)

def login(request):
    return render(request , 'login.html ')
