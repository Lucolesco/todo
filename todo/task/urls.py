from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from task.views import MainView
from django.contrib import admin
from django.urls import path

app_name = 'todo'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' ,MainView.as_view(), name="page/index"),
]

urlpatterns += staticfiles_urlpatterns()
