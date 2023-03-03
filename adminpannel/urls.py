from django.urls import path
from . import views
from django.views.generic.base import RedirectView

urlpatterns = [
     path('',views.admindashboard, name='dashboard'),
     path('adminlogin', views.loginadmin, name='adminlogin'),
     path('logout', views.logout, name='logout'),
     path('adminlogout', views.logoutadmin, name='adminlogout'),
     path('dashboard', views.admindashboard, name='admindashboard'),
     path('addcategorys', views.addcategorys, name='addcategorys'),
     path('addproducts', views.addproducts, name='addproducts'),
     path('addingcategory', views.addingcategory, name='addingcategory'),
     path('addingproduct', views.addingproduct, name='addingproduct'),
     path('viewproducts', views.viewproducts, name='viewproducts'),
     path('viewcategory',views.viewcategory, name='viewcategory'),
     path('removeproduct <id>', views.removeproduct, name='removeproduct'),
     path('editproduct <id>', views.editproduct, name='editproduct'),
     path('savingedit', views.savingedit, name='savingedit'),
     path('savingcatedit',views.savingcatedit, name='savingcatedit'),
     path('viewuser',views.viewuser, name='viewuser'),
     path('userdetail<int:user_id>',views.userdetail, name='userdetail'),
     path('deleteuser',views.deleteuser, name='deleteuser'),
     path('changestatususer',views.changestatususer,name='changestatususer'),
     path('todayssalesreport',views.todayssalesreport,name='todayssalesreport'),
     path('adminviewreports',views.adminviewreports,name='adminviewreports'),
     path('removecategory <id>', views.removecategory, name='removecategory'),
     path('editcategory <id>', views.editcategory, name='editcategory'),
     path('process',views.process, name='process'),
     path('dispatch',views.dispatch, name='dispatch'),
     path('deliver',views.deliver, name='deliver'),
     path('vieworder', views.vieworder,name='vieworder'),
     path('vieworder?status=Processing', views.vieworder,name='filtervieworder' ),
     path('vieworder?status=Ordered', views.vieworder,name='filtervieworder' ),
     path('vieworder?status=Dispatched', views.vieworder,name='filtervieworder' ),
     path('vieworder?status=Delivered', views.vieworder,name='filtervieworder' ),
     path('vieworder<str:stat>',views.vieworder,name='filtervieworder' ),


     ]