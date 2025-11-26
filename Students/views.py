from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from decouple import config

class StudentAPI(APIView):

    permission_classes = [IsAuthenticated]

    def get(self,request):

        all_student = Student.objects.all()

        student_data = Student_Task_Serializer(all_student, many = True).data

        return Response(student_data)
    
    def post(self, request):

        new_student = Student(name = request.data['name'],age = request.data['age'])

        new_student.save()

        return Response("New Student Created")

    def put(self,request,student_id):

        student_data = Student.objects.filter(id = student_id)

        student_data.update(name = request.data['name'],age = request.data['age'])

        return Response("Student data updated")
    
    def delete(self,request,student_id):

        student_data = Student.objects.get(id = student_id)

        student_data.delete()

        return Response("Student data deleted")
    
class TaskView(APIView):

    def get(self,request, task_id = None):

        if task_id == None:

            all_task = Task.objects.all()

            task_data = Task_Data_Serializer(all_task, many=True).data

            return Response(task_data)
        
        else:

            task = Task.objects.get(id = task_id)
            
            task_data = Task_Data_Serializer(task).data
            
            return Response(task_data)            

    def post(self, request):

        new_task = Task(student_reference_id = request.data['student_reference'], task_name = request.data['task_name'], description = request.data['description'])
        
        new_task.save()

        return Response('Task Created')
        
    def patch(self,request,task_id):

        task = Task.objects.get(id = task_id)

        update_task = Task_Serializer(task, data = request.data, partial = True)

        if update_task.is_valid():

            update_task.save()

            return Response("Task Updated")
        
        else:

            return Response(update_task.errors)
        
    def put(self,request,task_id):

        task = Task.objects.get(id = task_id)

        update_task = Task_Serializer(task, data = request.data, partial = True)

        if update_task.is_valid():

            update_task.save()

            return Response("Task Updated")
        
        else:

            return Response(update_task.errors)
        
    def delete(self,request, task_id):

        task = Task.objects.get(id = task_id)

        task.delete()

        return Response("Task deleted")

class RankSheetView(APIView):

    def get(self, request, id = None):

        if id == None:

            all_rank = RankSheet.objects.all()

            rank_data = RankSheet_Serializer(all_rank, many = True).data

            return Response(rank_data)
        
        else:

            rank = RankSheet.objects.get(id = id)

            rank_data = RankSheet_Serializer(rank).data

            return Response(rank_data)

    def post(self,request):

        total_marks = request.data['tamil'] + request.data['english'] + request.data['maths'] + request.data['science'] + request.data['social_science']

        average_marks = total_marks / 5

        if (request.data['tamil'] >=35) and request.data['english'] >=35 and request.data['maths'] >=35 and request.data['science'] >=35 and request.data['social_science']:

            student_result = True

        else:

            student_result = False

        new_data = RankSheet(tamil = request.data['tamil'], english = request.data['english'], maths = request.data['maths'], science = request.data['science'], social_science = request.data['social_science'], total = total_marks, average = average_marks, result = student_result)

        new_data.save()

        return Response("Data Saved")
    
    def patch(self,request,id):

        rank_data = RankSheet.objects.filter(id = id)

        total_marks = request.data['tamil'] + request.data['english'] + request.data['maths'] + request.data['science'] + request.data['social_science']

        average_marks = total_marks / 5

        if (request.data['tamil'] >= 35) and (request.data['english'] >=35) and (request.data['maths'] >=35) and (request.data['science'] >=35) and (request.data['social_science'] >=35):

            student_result = True
        
        else:

            student_result = False

        rank_data.update(tamil = request.data['tamil'], english = request.data['english'], maths = request.data['maths'], science = request.data['science'],social_science = request.data['social_science'], total = total_marks, average = average_marks, result = student_result)

        return Response("Data Updated")
    
    def delete(self, request, id):

        rank = RankSheet.objects.get(id = id)

        rank.delete()

        return Response("Data Deleted")