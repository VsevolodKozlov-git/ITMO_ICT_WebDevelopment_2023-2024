from django.urls import path
from project_first_app import views

app_name='project_first_app'
urlpatterns = [
    path("owner_detail/<int:pk>", views.OwnerDetail.as_view(), name='owner_info'),
    path("owner_list", views.OwnerList.as_view(), name='owner_list'),
    # path("owner_form", views.OwnerForm.as_view(), name='owner_form'),
    path('owner_form', views.OwnerForm.as_view(), name='owner_form'),
    path("car_detail/<int:pk>", views.CarDetail.as_view(), name='car_detail'),
    path("car_form", views.CarCreateView.as_view(), name='car_form'),
    path("car_update/<int:pk>", views.CarUpdateView.as_view(), name='car_update'),
    path("car_delete/<int:pk>", views.CarDeleteView.as_view(), name='car_delete')
]

