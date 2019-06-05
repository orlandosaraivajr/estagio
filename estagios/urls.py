from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from estagios import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('estagios.core.urls')),
    path('alunos/', include('estagios.aluno.urls')),
    ]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
