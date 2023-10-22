from django.urls import path
from app_studentPresent.views.views import AddNewStudent, ShowNewStudent, delete_data, update_data
from app_studentPresent.views.filliere import addNewfil, delete_data_fil, update_data_fil
from app_studentPresent.views.faculte import addNewfac, delete_data_fac, update_data_fac

urlpatterns = [
    path('show', ShowNewStudent.as_view(), name="show"),
    path('add_new', AddNewStudent, name="add_new"),
    path('delete/<int:id>/', delete_data, name="deletedata"),
    path('<int:id>/', update_data , name="updatedata"),
    #path for faculté
    path('add_new_fac', addNewfac, name="add_new_fac"),
    path('deletefac/<int:id>/', delete_data_fac, name="deletedata_fac"),
    path('updatedata_fac/<int:id>/', update_data_fac , name="updatedata_fac"),
    #path for filliere
    path('add_new_fil', addNewfil, name="add_new_fil"),
    path('deletefil/<int:id>/', delete_data_fil, name="deletedata_fil"),
    path('updatedata_fil<int:id>/', update_data_fil , name="updatedata_fil"),
]
