from django.shortcuts import render
from .models import ToDoItem
from .serializers import ToDoItemSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


def index(request):
    return render(request, 'todo/index.html')


@api_view(['GET', 'POST', 'DELETE'])
def todo_item_list(request):
    if request.method == 'GET':
        todo_items = ToDoItem.objects.all()
        serializer = ToDoItemSerializer(todo_items, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ToDoItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        ToDoItem.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['PATCH'])
def todo_item_detail(request, pk):
    try:
        todo_item = ToDoItem.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = ToDoItemSerializer(todo_item, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)