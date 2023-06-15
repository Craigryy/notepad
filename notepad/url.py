from django.urls  import path
from .views import get_note

urlpatterns =[
    path('Notes/<int:id>/',get_note)
]