"""
SITE:
category -> 5
category children -> 
word list
word detail
profile
favourite words
"""

"""
ADMIN:
word,
category,
user
"""

from django.shortcuts import render
from .models import Profile


# Create your views here.
def profile_detail(request):
    profile = Profile.objects.all()
    return render(request, 'profile.html', {'profile': profile})
