from .serializers import StudentSerializer
from .models import Student 
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, ListCreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly,DjangoModelPermissions

#combined views:

class StudentListCreate(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [DjangoModelPermissions]

    # # to set authentication and permission classes dynamically
    # def get_permissions(self):
    #     if self.request.method == 'GET':
    #         self.permission_classes = [AllowAny]
    #     elif self.request.method == 'POST':
    #         self.permission_classes = [IsAuthenticated]
    #     return super().get_permissions()

class StudentRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
 

