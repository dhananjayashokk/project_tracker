from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .. models import *
from .. serializers import *



@api_view(['GET','POST'])
def log_entry(request):

	if request.method == 'GET':
		project_id = request.GET['project_id']
		logs = LogEntries.objects.filter(project_id=project_id)
		serializer = LogEntrieserializer(logs, many=True)
		return Response(serializer.data)

	elif request.method == 'POST':	
		serializer = LogEntrieserializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

