from django.conf.urls import url
from . import views
app_name="quizzz"
urlpatterns=[
# url(r'^register/$',views.register,name='register'),
# url(r'^login/$',views.user_login,name='user_login'),
url(r'^qp$',views.qp,name="questionpage"),
url(r'^qps$',views.qp1,name="qps1")
]
