from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('ngo-volunteer/', views.NgoVolunteerView.as_view(), name='ngovolunteerview'),
    path('map-view/', views.MapView.as_view(), name='mapview'),
    path('request/', views.CreateRequest.as_view(), name='requestview'),
    # path('volunteer/', views.Maintenance.as_view(), name='registerview'),
    path('volunteer/', views.RegisterVolunteer.as_view(), name='registerview'),
    path('NGO/', views.RegisterNGO.as_view(), name='ngoregisterview'),
    path('NGO/download/', views.download_ngo_list, name='ngo_download_view'),
    path('requests/', views.request_list, name='requestlistview'),
    url(r'request_details/(?P<request_id>\d+)/$', views.request_details, name='requestdetailsview'),
    path('contactus/', views.districtmanager_list, name='contactus'),
    path('reg_success/', views.RegSuccess.as_view(), name='reg_successview'),
    path('req_sucess/', views.ReqSuccess.as_view(), name='req_sucessview'),
    path('district_needs/', views.DistNeeds.as_view(), name='distneedsview'),
    path('reg_contrib/', views.RegisterContributor.as_view(), name='reg_contribview'),
    path('contrib_success/', views.ContribSuccess.as_view(), name='contribsucessview'),
    path('disclaimer/', views.DisclaimerPage.as_view(), name='disclaimer'),
    path('ieee/', views.AboutIEEE.as_view(), name='aboutieee'),
    path('data/' , views.mapdata , name="mapdata"),
    path('map/' , views.mapview , name="mapview"),
    path('dmodash/' , views.dmodash , name="DMODash"),
    path('dmoinfo/' , views.dmoinfo , name="DMOInfo" ),
    path('error/' , views.error , name="errorview" ),
    path('login/', auth_views.LoginView.as_view(template_name='mainapp/login.html'),name='user_login'),
    path('logout/', views.logout_view, name='user_logout'),
    path('relief_camps/', views.relief_camps, name='relief_camps'),
    path('relief_camps_list', views.relief_camps_list, name='relief_camps_list'),
    path('camp/<int:pk>/requirements/',views.CampRequirements.as_view(),name='camp_requirements'),
    path('camp/<int:pk>/details/',views.CampDetails.as_view(),name='camp_details'),
    path('camp/<int:camp_id>/add_person/', views.AddPerson.as_view(), name='add_person'),
    path('coordinator_home/', views.coordinator_home, name='coordinator_home'),
    path('find_people/', views.find_people, name='find_people'),
    path('announcements/', views.announcements, name="Announcements"),
    path('camp_requirements/', views.camp_requirements_list, name='camp_requirements_list')
]
