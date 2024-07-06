# from django.shortcuts import render
# from django.contrib.auth.decorators import login_required
# from .models import Profile
#
#
# # Create your views here.
# def profile_detail(request):
#     profile = Profile.objects.all()
#     name = profile.first('age')
#     context = {'name': name}
#     return render(request, 'profile.html', context)

# from django.shortcuts import render
# from .models import Profile
#
#
# def profile_detail(request):
#     profiles = Profile.objects.all()  # Fetch all profiles (assuming there's only one in your case)
#     profile = profiles.first()  # Get the first profile object
#     age = profile.age if profile else None  # Get age if profile exists, otherwise None
#     context = {'age': age}
#     return render(request, 'profile.html', context)

from django.shortcuts import render
from .models import Profile


def profile_detail(request):
    # request.user
    # Assuming you want to fetch the profile with username 'admin'
    profile = Profile.objects.filter(username='09390605460').first()
    user_name = profile.username
    first_name = profile.first_name
    last_name = profile.last_name
    email = profile.email
    image = profile.image
    age = profile.age
    context = {'user_name': user_name, 'first_name': first_name, 'last_name': last_name, 'email': email, 'image': image,
               'age': age}
    return render(request, 'profile.html', context)


def profile_like(request):
    profile: Profile = request.user
    liked_words = profile.liked_words.all()
    context = {'liked_words': liked_words}
    return render(request, 'likes.html', context)
