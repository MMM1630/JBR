from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from jbr.views import AboutUsView, GuaranteeView, FoundersView, VolunteerView, \
    DokumentView, NeedyView, NewsView, NeedyProfileView,ContactsView
from rest_framework import permissions
# from .sitemap import SitemapView


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


urlpatterns = [
    path("Нуждающийся", NeedyView.as_view()),
    path("О нас", AboutUsView.as_view()),
    path("Гарантия", GuaranteeView.as_view()),
    path("Основатели", FoundersView.as_view()),
    path('Валантеры', VolunteerView.as_view()),
    path('Сертификаты', DokumentView.as_view()),
    path('Новости', NewsView.as_view()),
    path('Личный кабинет', NeedyProfileView.as_view()),
    path('Контакты', ContactsView.as_view()),
    path('ЖБР', schema_view.with_ui('swagger', cache_timeout=0)),
    # path("sitemap.xml", SitemapView.as_view()),
]
