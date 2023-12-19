"""Django API urlpatterns declaration for {{ cookiecutter.app_name }} app."""

from nautobot.apps.api import OrderedDefaultRouter

from {{ cookiecutter.app_name }}.api import views

router = OrderedDefaultRouter()
# add the name of your api endpoint, usually hyphenated model name in plural, e.g. "my-model-classes"
router.register("{{ cookiecutter.model_class_name.lower() }}", views.{{ cookiecutter.model_class_name }}ViewSet)

urlpatterns = router.urls
