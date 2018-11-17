from django.urls.conf import url, include
from accounts.views import index, logout, login, register, user_profile
import url_reset

urlspatterns=[
    url(r'^$', index, name ="index"),
    url(r'^login/$', login, name ="login"),
    url(r'^logout/$', logout, name="logout"),
    url(r'^register/$', register, name="register"),
    url(r'^user_profile/$', user_profile, name ="user_profile"),
    url(r'^password-reset/$', include(url_reset))
    ]