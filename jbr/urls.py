from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.routers import DefaultRouter
from jbr.views import AboutUsView, GuaranteeView, FoundersView, VolunteerView, DokumentView, NewsView, NeedyProfileView, VolunteerView, VolunteerAssignment, ContactsView, HelpedNeedyView, BankView, ApplicationView

schema_view = get_schema_view(
    openapi.Info( 
        title="ЖБР.kg",
        default_version='v1',
        description="Документация Жакшылыктын биримдик реестрери",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@yourapi.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

router = DefaultRouter()

router.register(r'needy_profile', NeedyProfileView, basename='needy_profile')
router.register(r'volunteer_assignments', VolunteerAssignment, basename='volunteer_assignment')

urlpatterns = [
    path("AboutUs", AboutUsView.as_view()),
    path("Guarentee", GuaranteeView.as_view()),
    path("Founders", FoundersView.as_view()),
    path('Volunteer', VolunteerView.as_view()),
    path('Dokument', DokumentView.as_view()),
    path('News', NewsView.as_view()),
    path('Contacts', ContactsView.as_view()),
    path('Helped_Needy', HelpedNeedyView.as_view()),
    path("Bank", BankView.as_view()),
    path("Aplication", ApplicationView.as_view()),
    path('JBR', schema_view.with_ui('swagger', cache_timeout=0)),
    path('api/', include(router.urls)),
]
