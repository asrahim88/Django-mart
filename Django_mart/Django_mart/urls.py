from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views
urlpatterns = [
    path("", views.home, name= 'home'),
    path('admin/', admin.site.urls),
    path('account/', include("accounts.urls")),
    path('cart/', include("cart.urls")),
    # path('category/', include("category.urls")),
    path('orders/', include("orders.urls")),
    path('store/', include("store.urls")),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
