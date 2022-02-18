from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from user.models import ExtendUser


class HomePageListView(LoginRequiredMixin, ListView):
    template_name = 'home/home_page.html'
    model = ExtendUser
    context_object_name = 'all_ext_user'
