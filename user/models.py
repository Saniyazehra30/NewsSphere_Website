from django.db import models

# Create your models here.

# jis naam ka table us naam ka class bnega
# jis naam ka funtion bnaya hai us naam ka table nhi

class contactus(models.Model):
    Name= models.CharField(max_length=30,null=True)
    Email= models.EmailField(max_length=50,null=True)
    Mobile= models.CharField(max_length=14,null=True)
    Message= models.TextField(null=True)

class Category(models.Model):
    category_name=models.CharField(max_length=100,null=True)
    category_img=models.ImageField(upload_to='static/category/',null=True)
    def __str__(self):
        return self.category_name

class slider(models.Model):
    picture=models.ImageField(upload_to='static/category/',null=True)
    title=models.CharField(max_length=40,null=True)
    descrp=models.TextField(null=True)

class Jobs(models.Model):
    jtitle = models.CharField(max_length=40, null=True)
    jlink =  models.CharField(max_length=150, null=True)
    jposted_date =  models.DateField(null=True)

class city_news(models.Model):
    city_name =models.CharField(max_length=40, null=True)
    city_pic = models.ImageField(upload_to='static/city_news/',null=True)
    def __str__(self):
        return self.city_name

class News(models.Model):
    headline = models.CharField(max_length=400, null=True)
    news_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    news_city = models.ForeignKey(city_news, on_delete=models.CASCADE)
    news_descrp = models.TextField(null=True)
    posted_date =  models.DateField()
    news_pic = models.ImageField(upload_to='static/news/',null=True)

class vdo_news(models.Model):
    vdo_headline = models.CharField(max_length=400, null=True)
    vdo_news_descrp = models.TextField(null=True)
    vdo_link = models.CharField(max_length=70, null=True)
