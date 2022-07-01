from django.contrib import admin
from django.urls import include, path
from tickets import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register('guests', views.view_guest)
router.register('movie', views.view_movie)
router.register('reservations', views.view_reservation)
urlpatterns = [
    path('admin/', admin.site.urls),
    #path('',views.no_rest_models)
    #path('',views.no_rest)
    path('',views.FBV_list),
    path('rest/<int:pk>/',views.FBV_pk),
    path('s',views.CBV_list.as_view()),
    path('k/<int:pk>/',views.CBV_pk.as_view()),
    path('ss',views.mixins_list.as_view()),
    path('kk/<int:pk>/',views.mixins_pk.as_view()),
    path('z',views.generics_list.as_view()),
    path('zz/<int:pk>',views.generics_pk.as_view()),
    path('view/',include(router.urls)),
    path('fbv/findmovie', views.find_movie),
    path('newres',views.new_reservation),
    path('auth',include('rest_framework.urls')),
    path('token',obtain_auth_token),
    path('post/<int:pk>',views.Post_pk.as_view()),
]
