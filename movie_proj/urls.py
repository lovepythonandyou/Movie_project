from django.contrib import admin
from django.urls import path, include

admin.site.site_header = 'Наша админка'
admin.site.index_title = 'Наша супер админка'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('movie_app.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
]
