"""Django urlpatterns declaration for {{ cookiecutter.plugin_name }} plugin."""
from nautobot.apps.urls import NautobotUIViewSetRouter

from {{ cookiecutter.plugin_name }} import views


router = NautobotUIViewSetRouter()
router.register("{{ cookiecutter.model_class_name | lower }}", views.{{ cookiecutter.model_class_name }}UIViewSet)

urlpatterns = router.urls
