from django.contrib import admin
from django.urls import path
from . views import accounts,tracker


urlpatterns = [
	path('',accounts.index,name="home"),
	path('accounts/sign_up/',accounts.sign_up,name="sign-up"),
	path('log_entry',tracker.log_entry,name="log_entry")
]