from rest_framework import routers
from . import views

router = routers.SimpleRouter()
router.register('contact', views.ContactFormView)
urlpatterns = router.urls