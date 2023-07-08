from django.urls import path
from App import views

urlpatterns = [
    path('pdf/', views.render_pdf_view, name='rander_pdf_view'),   
]
