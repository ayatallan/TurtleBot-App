from django.urls import include,path
from users.views import dashboard,register
urlpatterns = [
    path("dashboard/", dashboard, name="dashboard"),
    path("accounts/", include("django.contrib.auth.urls")),
    path('oauth/', include('social_django.urls', namespace='social')), # <-- here
    path("register/", register, name="register"),
]