from django.urls import include, path
from rest_framework import routers
from . import views

# router = routers.DefaultRouter()
# router.register(r'heroes', views.HeroViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
# urlpatterns = [
#     path('', include(router.urls)),
#     path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
# ]

urlpatterns = [
    path('', views.heroList, name="heros"),
    path('detail/<str:pk>/', views.heroDetail, name="detail"),
    path('create', views.heroCreate, name="create"),
    path('update/<str:pk>/', views.heroUpdate, name="update"),
    path('delete/<str:pk>/', views.heroDelete, name="delete"),
    path('deleteAll', views.heroDeleteAll, name="deleteAll"),
    path('send', views.heroSend, name="send"),
]
