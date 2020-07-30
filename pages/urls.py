from django.urls import path

from .views import HomePageView, AboutCreatorView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('AboutMe/', AboutCreatorView.as_view(), name='AboutMe')
]