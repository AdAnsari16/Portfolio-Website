from django.urls import include, path
from my_contact_data import views
 
app_name = 'app_name'
 
urlpatterns = [
    path('home',views.home,name='home')
]
