from django.contrib import admin
from .models import About, Experience, Education, Certifications, Interests 
# Register your models here.

class AboutAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'address', 'phone')
admin.site.register(About, AboutAdmin)

class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'position', 'start_date', 'end_date')
admin.site.register(Experience, ExperienceAdmin)

class EducationAdmin(admin.ModelAdmin):
    list_display = ('school_name', 'degree', 'start_date', 'end_date', 'gpa')
admin.site.register(Education, EducationAdmin)

class CertificationsAdmin(admin.ModelAdmin):
    list_display = ('certificate_name', 'certificate_startdate', 'certificate_enddate', 'certificate_link')
admin.site.register(Certifications, CertificationsAdmin)

class InterestsAdmin(admin.ModelAdmin):
    list_display = ('interests',)
admin.site.register(Interests, InterestsAdmin)