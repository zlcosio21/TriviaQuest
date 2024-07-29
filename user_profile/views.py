from django.shortcuts import render


# Create your views here.
def profile(request):
    return render(request, "user_profile/profile.html")


def ranking(request):
    return render(request, "user_profile/ranking.html")