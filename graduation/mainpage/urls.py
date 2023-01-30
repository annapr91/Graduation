from django.urls import path

from .views import *

urlpatterns = [
    path('', first, name='first'),
    path('contact/', contact, name ='contact'),
path('logout/', logout_view, name ='logout'),
path('buildings/', KidsKindergarden.as_view(), name ='buildings'),
path('search/', Search.as_view(), name ='search'),
path('search/<int:sad_id>/', KindergardenInfo.as_view(), name ='sad'),
]