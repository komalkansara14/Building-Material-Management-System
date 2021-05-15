from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.home, name="home"),
    path('user_index/', views.index, name="index"),
    path('transporter_index/', views.transporter_index, name="transporter_index"),
    path('elements/', views.elements, name="elements"),
    path('generic/', views.generic, name="generic"),
    
    path('user_register/', views.user_register, name="user_register"),
    path('otp_verify/', views.otp_verify, name="otp"),
    path('login/', views.login, name="login"),
    path('user_forgot/', views.user_forgot, name='user_forgot'),
    path('forgot_otp/', views.forgot_otp, name='forgot_otp'),
    path('user_reset_password/', views.user_reset_password, name='user_reset_password'),
    path('change_password/', views.change_password, name="change_password" ),
    path('transpoter_change_password/', views.transporter_change_password, name="transporter_change_password" ),

    path('transporter_register/', views.transporter_register, name="transporter_register"),
    path('otp_verify_transporter/', views.otp_verify_transporter, name="otp_transporter"),
    path('transporter_login/', views.transporter_login, name="transporter_login"),
    path('transporter_forgot/', views.transporter_forgot, name="transporter_forgot"),
    path('transporter_forgot_otp/', views.transporter_forgot_otp, name="transporter_forgot_otp"),
    path('transporter_reset_password/', views.transporter_reset_password, name="transporter_reset_password"),
    
    path('godownstock/', views.godownstock, name="godownstock"),
    path('admin_login/', views.admin_login, name='admin_login'),
    path('seller/', views.seller, name='seller'),
    path('buy_now_cement/', views.buy_now_cement, name="buy_now_cement"),
    path('buy_now_sand/', views.buy_now_sand, name="buy_now_sand"),
    path('buy_now_bricks/', views.buy_now_bricks, name="buy_now_bricks"),

    path('order_bricks_details/', views.order_bricks_details, name="order_bricks_details"),
    path('order_sand_details/', views.order_sand_details, name="order_sand_details"),
    path('order_cement_details/', views.order_cement_details, name="order_cement_details"),

    path('pay/<int:pk>', views.initiate_payment, name='pay'),
    path('callback/', views.callback, name='callback'),
    
    path('logout/', views.logout, name='logout'),
    path('transporter_logout/', views.transporter_logout, name='transporter_logout'),
    path('cart/',views.cart,name='cart'),
    path('delete_item/<int:pk>',views.delete_item,name='delete_item'),
    path('update_order/<int:pk>', views.update_order, name='update_order'),
    path('my_order/', views.my_order, name="my_order"),
    path('delivery_details/',views.delivery_details, name = "delivery_details"),
    path('remaining_delivery/', views.remaining_delivery, name = "remaining_delivery"),
    path('completed_delivery/', views.completed_delivery, name = "completed_delivery"),
    path('update_delivery/<int:pk>', views.update_delivery, name='update_delivery'),
    path('complete_order/<int:pk>', views.complete_order, name="complete_order"),

]
