from django.contrib import admin
from django.urls import path
from app.views import add_item

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', add_item, name='add_item'),
]

