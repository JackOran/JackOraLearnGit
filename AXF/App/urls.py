from django.conf.urls import url

from App import views

urlpatterns = [
    url(r'^hello/', views.hello),
    url(r'^home/', views.home, name="home"),
    url(r'^market/', views.market, name="market"),
    url(r'^market_with_params/(?P<typeid>\d+)/(?P<childcid>\d+)/(?P<order_rule>\d+)/', views.marketWithParams, name="market_with_params"),
    url(r'^add_to_cart/', views.add_to_cart, name="add_to_cart"),
    url(r'^cart/', views.cart, name="cart"),
    url(r'^mine/', views.mine, name="mine"),
    url(r'^user_register/', views.user_register, name="user_register"),
    url(r'^user_log_out/', views.user_log_out, name="user_log_out"),
    url(r'^check_user/', views.check_user, name="check_user"),
    url(r'^user_log_in/', views.user_log_in, name="user_log_in"),
    url(r'^sub_from_cart/', views.sub_from_cart, name="sub_from_cart"),
    url(r'^add_from_cart/', views.add_from_cart, name="add_from_cart"),
    url(r'^sub_to_cart/', views.sub_to_cart, name="sub_to_cart"),
    url(r'^change_cart_status/', views.change_cart_status, name="change_cart_status"),
    url(r'^change_status_multi/', views.change_status_multi, name="change_status_multi"),
    url(r'^change_status_multi_select/', views.change_status_multi_select, name="change_status_multi_select"),
    url(r'^generate_order/',views.generate_order, name="generate_order"),
    url(r'^orderdetail/', views.orderdetail, name="orderdetail"),
    url(r'^alipy/', views.alipy, name="alipy"),
    url(r'^order_list_wait_pay/', views.order_list_wait_pay, name="order_list_wait_pay"),
    url(r'^test_email/', views.test_email, name="test_email"),
    url(r'^user_active/', views.user_active, name="user_active"),
]