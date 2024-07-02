"""Django urlpatterns declaration for {{ cookiecutter.app_name }} app."""

from nautobot.apps.urls import NautobotUIViewSetRouter

from {{ cookiecutter.app_name }} import views

router = NautobotUIViewSetRouter()
router.register("{{ cookiecutter.model_class_name | lower }}", views.{{ cookiecutter.model_class_name }}UIViewSet)

urlpatterns = router.urls
