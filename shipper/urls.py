from django.conf.urls import url
from shipper.views import upload_report, task_list, custom_task_list

app_name = "shipper"
urlpatterns = [
    url(r'^upload/$', upload_report, name='upload_report'),
    url(r'^tasks/$', task_list, name='task_list'),
    url(r'^custom_tasks/$', custom_task_list, name='custom_task_list')
]
