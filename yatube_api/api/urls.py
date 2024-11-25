from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token

app_name = 'api'

v1_urls = [
    path('api-token-auth/', obtain_auth_token),
]


urlpatterns = [
    path('v1/', include(v1_urls)),
]
