from django.urls import path
from config import settings
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from jbr.views import PatientsView, AboutUsView, GuaranteeView, FoundersView, BankDetailsView
from django.conf.urls.static import static
from rest_framework import permissions



schema_view = get_schema_view(
    openapi.Info(
        title="Жакшылыктын биримдик реестрери",
        default_version='v1',
        description="Документация Жакшылыктын биримдик реестрери",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@yourapi.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path("patients", PatientsView.as_view()),
    path("about_us", AboutUsView.as_view()),
    path("guarantee", GuaranteeView.as_view()),
    path("founders", FoundersView.as_view()),
    path("bank_details", BankDetailsView.as_view()),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)