from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse

# Create your views here.

#function based view
def student_detail(request, id):
    stu = Student.objects.get(id = id)                       #getting the student object with id 1
    # print(stu)
    serializer = StudentSerializer(stu)                     #passing the student object to serializer
    # print(serializer)
    # print(serializer.data)
    json_data = JSONRenderer().render(serializer.data)        #converting the data to json
    # return HttpResponse(json_data, content_type='application/json')  #returning the json data
    return JsonResponse(serializer.data)  #returning the json data


#query set - all student data
def student_list(request):
    stu = Student.objects.all()                      #getting the student object with id 1
    # print(stu)
    serializer = StudentSerializer(stu, many=True)                     #passing the student object to serializer
    # print(serializer)
    # print(serializer.data)
    json_data = JSONRenderer().render(serializer.data)        #converting the data to json
    return HttpResponse(json_data, content_type='application/json')  #returning the json data
 