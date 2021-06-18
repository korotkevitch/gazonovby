from django.contrib import admin


from .models import Gallery
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('image_1_preview', 'intro', 'header', 'title', 'id', 'image_2_preview', 'image_big_preview', 'service', 'description')
admin.site.register(Gallery, GalleryAdmin)


from .models import Head
class HeadAdmin(admin.ModelAdmin):
    list_display = ('image_preview', 'logo_preview', 'welcome', 'text')
admin.site.register(Head, HeadAdmin)


from .models import About
class AboutAdmin(admin.ModelAdmin):
    list_display = ('intro', 'title', 'text')
admin.site.register(About, AboutAdmin)


from .models import Service
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('service', 'intro', 'title', 'description', 'icon')
admin.site.register(Service, ServiceAdmin)


from .models import Testimonial
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'testimonial')
admin.site.register(Testimonial, TestimonialAdmin)


from .models import Contact
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'message')
admin.site.register(Contact, ContactAdmin)