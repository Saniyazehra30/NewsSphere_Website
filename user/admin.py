from django.contrib import admin
from .models import *
# Register your models here.

class contactusAdmin(admin.ModelAdmin):
    list_display = ('Name','Email','Mobile','Message')
admin.site.register(contactus,contactusAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','category_name','category_img')
admin.site.register(Category,CategoryAdmin)

class sliderAdmin(admin.ModelAdmin):
    list_display = ('picture', 'title', 'descrp')
admin.site.register(slider,sliderAdmin)

class JobsAdmin(admin.ModelAdmin):
    list_display = ('id','jposted_date', 'jtitle', 'jlink')
admin.site.register(Jobs,JobsAdmin)

class city_newsAdmin(admin.ModelAdmin):
    list_display = ('id', 'city_name', 'city_pic')
admin.site.register(city_news,city_newsAdmin)

class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'posted_date','news_pic', 'headline','news_descrp', 'news_category', 'news_city' )
admin.site.register(News,NewsAdmin)

class vdo_newsAdmin(admin.ModelAdmin):
    list_display = ('vdo_headline','vdo_news_descrp' , 'vdo_link')
admin.site.register(vdo_news,vdo_newsAdmin)

