from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from home.StudentViewset import StudentViewset,CustomerViewset
from home import views
router = routers.DefaultRouter()
router.register(r'student', StudentViewset)
router.register(r'customer', CustomerViewset)
urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('useapi/', views.useapi),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
