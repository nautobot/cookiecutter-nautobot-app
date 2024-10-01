"""Django urlpatterns declaration for {{ cookiecutter.app_name }} app."""

from django.templatetags.static import static
from django.urls import path
from django.views.generic import RedirectView
from nautobot.apps.urls import NautobotUIViewSetRouter

from {{ cookiecutter.app_name }} import views

router = NautobotUIViewSetRouter()
router.register("{{ cookiecutter.model_class_name | lower }}", views.{{ cookiecutter.model_class_name }}UIViewSet)

urlpatterns = [
    path("docs/", RedirectView.as_view(url=static("{{ cookiecutter.app_name }}/docs/index.html")), name="docs"),
]

urlpatterns += router.urls
