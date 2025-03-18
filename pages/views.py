from django.shortcuts import render
from .models import About, Experience,Education, Interests, Certifications
# Create your views here.
def index(request):
    about = About.objects.first()
    experiences = Experience.objects.all().order_by('end_date')
    educations = Education.objects.all().order_by('-end_date')
    interests = Interests.objects.first()
    certifications = Certifications.objects.all()
    context = {
        'about': about,
        'experiences': experiences,
        'educations': educations,
        'interests': interests,
        'certifications': certifications
    }
    return render(request, 'pages/index.html', context)

