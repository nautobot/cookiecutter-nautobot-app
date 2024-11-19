"""Django urlpatterns declaration for {{ cookiecutter.app_name }} app."""

from django.templatetags.static import static
from django.urls import path
from django.views.generic import RedirectView
from nautobot.apps.urls import NautobotUIViewSetRouter

{% if cookiecutter.model_class_name != "None" %}
from {{ cookiecutter.app_name }} import views
{% else %}
# Uncomment the following line if you have views to import
# from {{ cookiecutter.app_name }} import views
{% endif %}

router = NautobotUIViewSetRouter()
{% if cookiecutter.model_class_name != "None" %}
router.register("{{ cookiecutter.model_class_name | lower }}", views.{{ cookiecutter.model_class_name }}UIViewSet)
{% else %}
# Here is an example of how to register a viewset, you will want to replace views.{{ cookiecutter.camel_name }}UIViewSet with your viewset
# router.register("{{ cookiecutter.app_name }}", views.{{ cookiecutter.camel_name }}UIViewSet)
{% endif %}

urlpatterns = [
    path("docs/", RedirectView.as_view(url=static("{{ cookiecutter.app_name }}/docs/index.html")), name="docs"),
]

urlpatterns += router.urls
