from django.urls import path,include
from . import views
urlpatterns = [
    path('viewstudents',views.viewstudents,name='viewstudents'),
    path('addstudents',views.addstudents,name='addstudents'),
    path('editstudents/<int:id>',views.editstudents,name='editstudents'),
    path('update/<int:id>',views.update,name="update"),
    path('deletestudents/<int:id>',views.deletestudents,name="deletestudents"),
]