from django.urls import path
from . import views

urlpatterns = [
    # Class-based views (DRF)
    path("", views.MusicianListCreateView.as_view(), name="manage-list"),
    path(
        "musicians/<int:pk>/", views.MusicianDetailView.as_view(),
        name="manage-detail"
    ),
    # Function-based views (alternative)
    path(
        "musicians-fbv/", views.musician_list, name="musician-list-fbv"
    ),
    path(
        "musicians-fbv/<int:pk>/", views.musician_detail,
        name="musician-detail-fbv"
    ),
]

app_name = "musician"
