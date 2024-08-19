from django.urls import path
from .views import *
urlpatterns = [

    path('add/',add_interview,name='add_interview'),
    path('all_data/',all_data,name='all_data'),
    path('',only_five,name='home'),
    path('interview_detail/<int:pk>/',interview_detail,name='interview_detail'),
    path('edit/<pk>/',edit,name='edit'),
    path('delete/<pk>',delete,name='delete'),
    path('hr_call/',with_hr,name='with_hr'),
    path('with_hr_entry/',with_hr_entry,name='with_hr_entry'),
    path('edit_hr_entry/<pk>/',edit_hr_entry,name='edit_hr_entry'),
    path('delete_hr_entry/<pk>/',delete_hr_entry,name='delete_hr_entry'),
    path('only_five/',only_five,name='only_five'),
path('search_by_date/', search_by_date, name='search_by_date'),

]
