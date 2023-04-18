from django.urls import path
from . import views

app_name = 'set_a_goal'

urlpatterns = [
    path('', views.index, name='index'),
    # ... (the rest of your urlpatterns)
]
