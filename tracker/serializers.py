from rest_framework import serializers
from .models import *

class LogEntrieserializer(serializers.ModelSerializer):
	class Meta:
		model=LogEntries
		fields=('project_id','task_name','start_time','end_time')
