from django.urls import path
from musician.views import (
    MusicianListCreateView,
    MusicianDetailView,
    musician_list,
    musician_detail
)

urlpatterns = [
    # Class-based views (DRF)
    path("", MusicianListCreateView.as_view(), name="manage-list"),
    path(
        "<int:pk>/", MusicianDetailView.as_view(),
        name="manage-detail"
    ),
    # Function-based views (alternative)
    path(
        "musicians-fbv/", musician_list, name="musician-list-fbv"
    ),
    path(
        "musicians-fbv/<int:pk>/", musician_detail,
        name="musician-detail-fbv"
    ),
]

app_name = "musician"
