from django.contrib import admin
from django.urls import include, path, re_path


urlpatterns = [
    path('admin/', admin.site.urls),
    #path('backoffice/', include(task_resource.urls)),
    #path('', include('backoffice.urls'))
    re_path('backoffice/(?P<version>(v1|v2))/', include('backoffice.urls'))
]



