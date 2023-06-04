
from django.urls import path
from ali import views
urlpatterns = [
    path('',views.home,name='home'),
    path('products', views.products, name='products'),
    path('category/<str:id>',views.category,name='category'),
    path('detail/<str:id>/<slug:slug>', views.detail,name='detail'),
    path('contact', views.contact, name='contact'),
    path('signout',views.signout,name='signout'),
    path('signin',views.signin,name='signin'),
    path('signup',views.signup,name='signup'),
    path('profile',views.profile,name='profile'),
    path('search',views.search,name='search'),
    path('profile_update',views.profile_update,name='profile_update'),
    path('password_update',views.password_update,name='password_update'),
    path('add_to_cart',views.add_to_cart,name='add_to_cart'),
    path('cart',views.cart,name='cart'),
    path('delete',views.delete,name='delete'),
    path('update',views.update,name='update'),
    path('checkout',views.checkout,name='checkout'),
    path('payment',views.payment,name='payment'),
    path('thankyou',views.thankyou,name='thankyou')

]