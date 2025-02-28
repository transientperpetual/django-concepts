from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .serializers import StudentSerializer
from .models import Student
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

#Function based views. This function will be called when the url is hit.
@csrf_exempt
def student_api(request):
    if request.method == 'GET':
        #convert the incoming json to python data
        json_data = request.body
        print('GET')
        print(json_data)
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id', None)

        #deserialize and send data back to client
        if id is not None:
            student = Student.objects.get(id=id)
            serializer = StudentSerializer(student)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type='application/json')
        print('GOTTA GIVE EM ALL')
        #if no id then send all data
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='application/json')

    # if method is post, read the data, convert to python data, then convert to complex type (serialize) and if valid then save it (insert in db)
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = StudentSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            ack = {'msg': 'Data Created'}
            json_data = JSONRenderer().render(ack)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')

    #if method is put, read the data, convert to python data, then convert to complex type (serialize) (partial update) and if valid then save it (update in db)
    if request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        #get data from db for the student with id
        student = Student.objects.get(id=id)
        #mark partial=True since this is a partial update
        serializer = StudentSerializer(student, data=python_data, partial=True)
        if serializer.is_valid():
            serializer.save()
            ack = {'msg': 'Data Updated'}
            json_data = JSONRenderer().render(ack)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')

    #if method is delete. read the id, and delete the student with that id, delete the row from db.
    if request.method == 'DELETE':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        student = Student.objects.get(id=id)
        student.delete()
        ack = {'msg': 'Data Deleted'}
        json_data = JSONRenderer().render(ack)
        return HttpResponse(json_data, content_type='application/json')