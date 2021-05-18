from django.urls import path
from .views import (
    CourseDeleteView,
    CourseListView,
    CourseUpdate,
    my_fbv,
    CourseView,
    CourseCreate
)

app__name='courses'
urlpatterns = [
    #path('',my_fbv,name='courses_list'),
    #path('',CourseView.as_view(template_name='contact.html'),name='CourseView'),
    path('<int:id>/',CourseView.as_view(),name='courses_detail'),
    path('',CourseListView.as_view(),name='course_list'),
    path('create/',CourseCreate.as_view(),name='course_create' ),
    path('<int:id>/update/',CourseUpdate.as_view(),name='course_update'),
    path('<int:id>/delete/',CourseDeleteView.as_view(),name='course_delete')
]
