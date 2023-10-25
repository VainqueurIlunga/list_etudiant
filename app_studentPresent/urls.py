from django.urls import path
from app_studentPresent.views.views import AddNewStudent, ShowNewStudent, delete_data, update_data
from app_studentPresent.views.filliere import addNewfil, delete_data_fil, update_data_fil
from app_studentPresent.views.faculte import addNewfac, delete_data_fac, update_data_fac
from app_studentPresent.views.promo_views import AddNewpromo, delete_data_pro, update_data_pro
from app_studentPresent.views.teachers import AddNewTeacher, delete_data_en, update_data_en
from app_studentPresent.views.cours import AddNewCourses, delete_data_cr, update_data_cr
from app_studentPresent.views.presence import AddNewPresence, delete_data_pre, update_data_pre

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
        #path for promotion
    path('add_new_pro', AddNewpromo, name="add_new_pro"),
    path('deletepro/<int:id>/', delete_data_pro, name="deletedata_pro"),
    path('updatedata_pro<int:id>/', update_data_pro , name="updatedata_pro"),
    # path for teacher
    path('add_new_en', AddNewTeacher, name="add_new_en"),
    path('deleteen/<int:id>/', delete_data_en, name="deletedata_en"),
    path('updatedata_en<int:id>/', update_data_en, name="updatedata_en"),
    # path for coursers
    path('add_new_cr', AddNewCourses, name="add_new_cr"),
    path('deletecr/<int:id>/', delete_data_cr, name="deletedata_cr"),
    path('updatedata_cr<int:id>/', update_data_cr, name="updatedata_cr"),
    # path for presence
    path('add_new_pre', AddNewPresence, name="add_new_pre"),
    path('deletepre/<int:id>/', delete_data_pre, name="deletedata_pre"),
    path('updatedata_pre<int:id>/', update_data_pre, name="updatedata_pre"),
]

