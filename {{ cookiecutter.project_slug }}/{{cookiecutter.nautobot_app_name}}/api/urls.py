"""Django API urlpatterns declaration for {{ cookiecutter.nautobot_app_name }}."""

from nautobot.core.api import OrderedDefaultRouter

from {{ cookiecutter.nautobot_app_name }}.api import views

router = OrderedDefaultRouter()
# add the name of your api endpoint, usually hyphenated model name in plural, e.g. "my-model-classes"
router.register("{{ cookiecutter.model_class_name.lower() }}", views.{{ cookiecutter.model_class_name }}ViewSet)


app_name = "{{ cookiecutter.nautobot_app_name }}-api"
urlpatterns = router.urls
