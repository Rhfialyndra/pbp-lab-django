from django.urls import path;
from wishlist.views import *;


app_name = 'wishlist'

urlpatterns = [
    path('ajax/add/', post_wishlist_json, name='post_wishlist_json'),
    path('ajax/', show_wishlist_ajax, name='show_wishlist_ajax'),
    path('json/', show_wishlist_json, name="show_wishlist_json"),
    path('xml/', show_wishlist_xml, name="show_wishlist_xml"),
    path('xml/<int:id>', show_wishlist_xml_by_id, name="show_wishlist_xml_by_id"),
    path('json/<int:id>', show_wishlist_json_by_id, name="show_wishlist_json_by_id"),
    path('register/', register, name="register"),
    path('login/', login_user, name="login_user"),
    path('logout/', logout_user, name='logout'),
]