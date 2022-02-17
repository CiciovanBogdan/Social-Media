from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import ListView

from user.models import ExtendUser


@login_required()
def home_page(request):
    user = request.user
    ext_user = ExtendUser.objects.filter(id=user.id)
    address = ext_user.values('address').first()['address']
    age = ext_user.values('age').first()['age']
    profile_pic = ext_user.values('profile_picture').first()['profile_picture']
    context = {
        'user': user,
        'profile_pic': profile_pic,
        'address': address,
        'age': age,
    }
    return render(request, 'home/home_page.html', context)


class HomePageListView(ListView):
    template_name = 'home/home_page.html'
    model = ExtendUser
    context_object_name = 'all_user'
