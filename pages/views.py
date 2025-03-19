from django.shortcuts import render
from .models import About, Experience,Education, Interests, Certifications
from django.db.models import Case, When, Value, BooleanField
# Create your views here.
def index(request):
    about = About.objects.first()
    experiences = Experience.objects.annotate(
        is_current=Case(
            When(end_date__isnull=True, then=Value(True)),
            default=Value(False),
            output_field=BooleanField(),

        )
    ).order_by('-is_current','-end_date')
    # experiences = Experience.objects.all().order_by('-start_date')
    educations = Education.objects.all().order_by('-start_date')
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

