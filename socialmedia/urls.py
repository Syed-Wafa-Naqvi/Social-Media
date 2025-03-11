from django.contrib import admin
from django.urls import path, include
from feed.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from feed.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('feed.urls')),
    path('', index, name='index'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
]