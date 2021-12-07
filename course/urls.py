from . import views
from django.urls import path

urlpatterns = [

    path('add', views.add_course),
    path('main', views.all_course),
    path('delete_course', views.delete_course),
    path('update_course/<int:course_id>', views.update_course),
    path('view_course', views.view_course),
    path('view_section', views.view_section),
    path('section', views.section),
    path('view_section_filter', views.view_section_filter),
    path('all', views.show_all),
    path('all_filter', views.all_filter),
    path('all_filter_location', views.all_filter_location),
    path('add_comment', views.add_comment),
    path('send_message', views.send_message_page),
    path('send', views.send_message),
    path('view_message', views.view_message)


]
