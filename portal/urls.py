from django.urls import path
from . import views

urlpatterns = [
    path('', views.checkauth, name='checkauth'),
    ]

urlpatterns += [ 
    path('allprojects/', views.allprojects, name='allprojects'),
    path('completedprojects/', views.completedprojects, name='completedprojects'),
    path('project/create/', views.ProjectDocumentinstanceCreate.as_view(), name='project_create'),
    path('project/<uuid:pk>', views.ProjectDetailView.as_view(), name='project-detail'),
    path('project/<uuid:pk>/ptsupdate/', views.ProjectDocumentinstanceUpdate.as_view(), name='project_update'),    
    path('project/<uuid:pk>/delete/', views.ProjectDelete.as_view(), name='project_delete'),    
    ]

urlpatterns += [ 
    path('users/', views.users, name='users'), 
    ]

urlpatterns += [ 
    path('exporting/', views.export, name='export'), 
    path('comexporting/', views.comexport, name='comexport'), 
    ]

urlpatterns += [
    path('countrylist/', views.CountryListView.as_view(), name='countrylist'),
    path('countrylist/create/', views.CountryCreate.as_view(), name='countrycreate'),
    path('countrylist/<uuid:pk>/edit/', views.CountryUpdate.as_view(), name='countryedit'),
    path('countrylist/<uuid:pk>/del/', views.CountryDelete.as_view(), name='countrydel'),
    path('citylist/', views.CityListView.as_view(), name='citylist'),
    path('citylist/create/', views.CityCreate.as_view(), name='citycreate'),
    path('citylist/<uuid:pk>/edit/', views.CityUpdate.as_view(), name='cityedit'),
    path('citylist/<uuid:pk>/del/', views.CityDelete.as_view(), name='citydel'),
]

urlpatterns += [
    path('createuser/', views.signup, name='signup'),
    path('userlist/', views.userlist, name='userlist'),
    path('userlist/<int:pk>/edit/', views.UpdateProfile.as_view(), name='userlistedit'),
    path('userlist/<int:pk>/changepassword/', views.change_password, name='pw_change'),
    path('userlist/<int:pk>/changepasswordstaff/', views.change_passwordstaff, name='pw_changestaff'),        
    path('userlist/<int:pk>/delete/', views.del_user, name='deleteuser'),
    path('userlist/<int:pk>/deletestaff/', views.del_userstaff, name='deleteuserstaff'),
]

urlpatterns += [
    path('userlist/<int:pk>/changeownpassword/', views.change_ownpassword, name='pw_ownchange'),    
]

urlpatterns += [
    path('success/', views.success, name='success'),    
]

urlpatterns += [ 
    path('groupcreate/', views.groupcreate, name='groupcreate'), 
    path('grouplist/', views.grouplist, name='grouplist'),
    path('grouplist/<int:pk>/update/', views.groupUpdate.as_view(), name='updategroup'),
    path('grouplist/<int:pk>/delete/', views.del_group, name='deletegroup'),
    ]

urlpatterns += [ 
    path('template/create/', views.templateCreate.as_view(), name='template_create'),
    path('template/<uuid:pk>/ptsupdate/', views.templateUpdate.as_view(), name='template_update'), 
    path('template/<uuid:pk>/delete/', views.templatesetdelete.as_view(), name='template_delete'), 
    path('templatelist/', views.TemplatesListView.as_view(), name='templatelist'),     
    ]


urlpatterns += [ 
    path('document/<uuid:pk>/', views.documentdetail.as_view(), name='document-detail'),
    path('document/<uuid:pk>/update/', views.documentupdate, name='documentupdate'),
    path('document/<uuid:pk>/comment/', views.documentcomment, name='documentcomment'),
    path('document/<uuid:pk>/delete/', views.documentdelete.as_view(), name='documentdelete'),
    path('document/<uuid:pk>/review/', views.ProjectDocumentreviewUpdate.as_view(), name='documentreview'),
    path('document/<uuid:pk>/review/success/', views.ProjectDocumentreviewsucess, name='documentreviewsuccess'),
    ]

urlpatterns += [ 
    path('project/<uuid:pk>/kom/mne/', views.documents, name='komne'),
    path('project/<uuid:pk>/cod/mne/', views.documents, name='cdmne'),
    path('project/<uuid:pk>/moc/mne/', views.documents, name='mdmne'),
    path('project/<uuid:pk>/dda/mne/', views.documents, name='ddamne'),
    path('project/<uuid:pk>/con/mne/', views.documents, name='cmne'),
    path('project/<uuid:pk>/pop/mne/', views.documents, name='popmne'),
    path('project/<uuid:pk>/ist/mne/', views.documents, name='istmne'),
    path('project/<uuid:pk>/com/mne/', views.documents, name='commne'),
    path('project/<uuid:pk>/kom/mne/create/', views.documentscreate, name='komnecreate'),
    path('project/<uuid:pk>/cod/mne/create/', views.documentscreate, name='codmnecreate'),
    path('project/<uuid:pk>/moc/mne/create/', views.documentscreate, name='modmnecreate'),
    path('project/<uuid:pk>/dda/mne/create/', views.documentscreate, name='ddamnecreate'),
    path('project/<uuid:pk>/con/mne/create/', views.documentscreate, name='conmnecreate'),
    path('project/<uuid:pk>/pop/mne/create/', views.documentscreate, name='popmnecreate'),
    path('project/<uuid:pk>/ist/mne/create/', views.documentscreate, name='istmnecreate'),
    path('project/<uuid:pk>/com/mne/create/', views.documentscreate, name='commnecreate'),
    path('project/<uuid:pk>/kom/mne/addtemplate/', views.addtemplate, name='komneaddtemplate'),
    path('project/<uuid:pk>/cod/mne/addtemplate/', views.addtemplate, name='codmneaddtemplate'),
    path('project/<uuid:pk>/moc/mne/addtemplate/', views.addtemplate, name='modmneaddtemplate'),
    path('project/<uuid:pk>/dda/mne/addtemplate/', views.addtemplate, name='ddamneaddtemplate'),
    path('project/<uuid:pk>/con/mne/addtemplate/', views.addtemplate, name='conmneaddtemplate'),
    path('project/<uuid:pk>/pop/mne/addtemplate/', views.addtemplate, name='popmneaddtemplate'),
    path('project/<uuid:pk>/ist/mne/addtemplate/', views.addtemplate, name='istmneaddtemplate'),
    path('project/<uuid:pk>/com/mne/addtemplate/', views.addtemplate, name='commneaddtemplate'),
    ]

urlpatterns += [ 
    path('project/<uuid:pk>/kom/idd/', views.documents, name='koid'),
    path('project/<uuid:pk>/cod/idd/', views.documents, name='cdid'),
    path('project/<uuid:pk>/moc/idd/', views.documents, name='mdid'),
    path('project/<uuid:pk>/dda/idd/', views.documents, name='ddaid'),
    path('project/<uuid:pk>/con/idd/', views.documents, name='cid'),
    path('project/<uuid:pk>/pop/idd/', views.documents, name='popid'),
    path('project/<uuid:pk>/ist/idd/', views.documents, name='istid'),
    path('project/<uuid:pk>/com/idd/', views.documents, name='comid'),
    path('project/<uuid:pk>/kom/idd/create/', views.documentscreate, name='koiscreate'),
    path('project/<uuid:pk>/cod/idd/create/', views.documentscreate, name='codidcreate'),
    path('project/<uuid:pk>/moc/idd/create/', views.documentscreate, name='modidcreate'),
    path('project/<uuid:pk>/dda/idd/create/', views.documentscreate, name='ddaidcreate'),
    path('project/<uuid:pk>/con/idd/create/', views.documentscreate, name='conidcreate'),
    path('project/<uuid:pk>/pop/idd/create/', views.documentscreate, name='popidcreate'),
    path('project/<uuid:pk>/ist/idd/create/', views.documentscreate, name='istidcreate'),
    path('project/<uuid:pk>/com/idd/create/', views.documentscreate, name='comidcreate'),
    path('project/<uuid:pk>/kom/idd/addtemplate/', views.addtemplate, name='koiddaddtemplate'),
    path('project/<uuid:pk>/cod/idd/addtemplate/', views.addtemplate, name='codiddaddtemplate'),
    path('project/<uuid:pk>/moc/idd/addtemplate/', views.addtemplate, name='modiddaddtemplate'),
    path('project/<uuid:pk>/dda/idd/addtemplate/', views.addtemplate, name='ddaiddaddtemplate'),
    path('project/<uuid:pk>/con/idd/addtemplate/', views.addtemplate, name='coniddaddtemplate'),
    path('project/<uuid:pk>/pop/idd/addtemplate/', views.addtemplate, name='popiddaddtemplate'),
    path('project/<uuid:pk>/ist/idd/addtemplate/', views.addtemplate, name='istiddaddtemplate'),
    path('project/<uuid:pk>/com/idd/addtemplate/', views.addtemplate, name='comiddaddtemplate'),
    ]

urlpatterns += [ 
    path('project/<uuid:pk>/kom/arc/', views.documents, name='koarc'),
    path('project/<uuid:pk>/cod/arc/', views.documents, name='cdarc'),
    path('project/<uuid:pk>/moc/arc/', views.documents, name='mdarc'),
    path('project/<uuid:pk>/dda/arc/', views.documents, name='ddarc'),
    path('project/<uuid:pk>/con/arc/', views.documents, name='carc'),
    path('project/<uuid:pk>/pop/arc/', views.documents, name='poparc'),
    path('project/<uuid:pk>/ist/arc/', views.documents, name='istarc'),
    path('project/<uuid:pk>/com/arc/', views.documents, name='comarc'),
    path('project/<uuid:pk>/kom/arc/create/', views.documentscreate, name='komarcreate'),
    path('project/<uuid:pk>/cod/arc/create/', views.documentscreate, name='codarccreate'),
    path('project/<uuid:pk>/moc/arc/create/', views.documentscreate, name='modarccreate'),
    path('project/<uuid:pk>/dda/arc/create/', views.documentscreate, name='ddaarccreate'),
    path('project/<uuid:pk>/con/arc/create/', views.documentscreate, name='conarccreate'),
    path('project/<uuid:pk>/pop/arc/create/', views.documentscreate, name='poparccreate'),
    path('project/<uuid:pk>/ist/arc/create/', views.documentscreate, name='istarccreate'),
    path('project/<uuid:pk>/com/arc/create/', views.documentscreate, name='comarccreate'),
    path('project/<uuid:pk>/kom/arc/addtemplate/', views.addtemplate, name='koarcaddtemplate'),
    path('project/<uuid:pk>/cod/arc/addtemplate/', views.addtemplate, name='codarcaddtemplate'),
    path('project/<uuid:pk>/moc/arc/addtemplate/', views.addtemplate, name='modarcaddtemplate'),
    path('project/<uuid:pk>/dda/arc/addtemplate/', views.addtemplate, name='ddaarcaddtemplate'),
    path('project/<uuid:pk>/con/arc/addtemplate/', views.addtemplate, name='conarcaddtemplate'),
    path('project/<uuid:pk>/pop/arc/addtemplate/', views.addtemplate, name='poparcaddtemplate'),
    path('project/<uuid:pk>/ist/arc/addtemplate/', views.addtemplate, name='istarcaddtemplate'),
    path('project/<uuid:pk>/com/arc/addtemplate/', views.addtemplate, name='comarcaddtemplate'),
    ]

#urlpatterns += [ 
#    path('project/<uuid:pk>/projectsuccess/', views.projectsuccess, name='projectsuccess'),
#    ]

urlpatterns += [ 
    path('test/', views.test, name='test'),
    ]