from django.urls import path,include
from . views import *
urlpatterns=[
        path('getpost',Student_view.as_view()),
        # path('student/',StudentApi.as_view()),
        # path('get_api',std),
        # path('student/',post_data),
        # path('update-student/<id>/' , update_student),
]