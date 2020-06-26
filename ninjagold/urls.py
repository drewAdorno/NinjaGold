from django.urls import path, include

urlpatterns = [
    path('', include('app1.urls')),
    path('/save', include('logReg.urls'))
]
