from django.core.urlresolvers import reverse_lazy
from django.views.generic import FormView, ListView
from shipper.forms import ReportUpload
from celery import current_app
from django_celery_results.models import TaskResult
from shipper.models import Task

app = current_app
# Create your views here.


class UploadReport(FormView):
    template_name = 'shipper/upload.html'
    form_class = ReportUpload
    success_url = reverse_lazy('shipper:upload_report')

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        # files = request.FILES.getlist('file')
        if form.is_valid():
            form.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class TaskList(ListView):
    queryset = TaskResult.objects.all()
    template_name = 'shipper/list.html'


class CustomTaskList(ListView):
    queryset = Task.objects.all()
    template_name = 'shipper/list.html'



task_list = TaskList.as_view()
custom_task_list = CustomTaskList.as_view()
upload_report = UploadReport.as_view()
