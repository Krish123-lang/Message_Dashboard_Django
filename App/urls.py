from django.urls import path, include
from . import views
from inbox import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.home, name="home"),

    path('login/', include('django.contrib.auth.urls')),

    # Path to send message
    path('send_message', views.send_message, name="send_message"),


    path("inbox/", views.inbox, name="inbox"),

    path('delete_message/<str:customer_id>', views.delete_message, name="delete_message"),

    path('customer/<str:customer_id>', views.customer, name="customer"),

    path("mark_message/", views.mark_message, name="mark_message"),

    path("autologout", views.AutoLogoutUser, name="autologout"),
    


] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

handler = 'App.views.E_500'
handler = 'App.views.E_404'