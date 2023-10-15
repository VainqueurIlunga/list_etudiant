from django.urls import path
from app_studentPresent.views import AddNewStudent, ShowNewStudent, delete_data, update_data

urlpatterns = [
    path('show', ShowNewStudent.as_view(), name="show"),
    path('add_new', AddNewStudent, name="add_new"),
    path('delete/<int:id>/', delete_data, name="deletedata"),
    path('<int:id>/', update_data , name="updatedata"),
     
    
    
]
