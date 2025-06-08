from django.http import JsonResponse, HttpResponseNotAllowed
from Todo.models import Todo
import json


from django.views.decorators.csrf import csrf_exempt

def todo_list(request):
    if request.method == 'GET':
        todos = list(Todo.objects.values())
        return JsonResponse(todos, safe=False) 
    else:
        return HttpResponseNotAllowed(['GET'])
    
@csrf_exempt
def  create_todo(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        todos = Todo.objects.create(
            task=data['task'],
            completed=data.get('completed', False)
        )
        return JsonResponse({
            'id': todos.id,
            'task': todos.task,
            'completed': todos.completed,
            'created': todos.created
        }, status=201)
    else:
        return HttpResponseNotAllowed(['POST'])

@csrf_exempt
def todo_detail(request, pk):
    try:
        todo_obj = Todo.objects.get(pk=pk)
    except Todo.DoesNotExist:
        return JsonResponse({'error': 'Todo not found'}, status=404)

    if request.method == 'GET':
        return JsonResponse({
            'id': todo_obj.id,
            'task': todo_obj.task,
            'completed': todo_obj.completed,
            'created': todo_obj.created
        })
    else:
        return HttpResponseNotAllowed(['GET'])
      
@csrf_exempt
def update_todo(request, pk):
    try:
        todo = Todo.objects.get(pk=pk)
    except Todo.DoesNotExist:
        return JsonResponse({'error': 'Todo not found'}, status=404)
    
    if request.method == 'PUT':
        data = json.loads(request.body)
        todo.task = data.get('task', todo.task)
        todo.completed = data.get('completed', todo.completed)
        todo.save()
        return JsonResponse({
            'id': todo.id,
            'task': todo.task,
            'completed': todo.completed,
            'created': todo.created
        })
    else:
        return HttpResponseNotAllowed(['PUT'])    

@csrf_exempt
def delete_todo(request, pk):
    try:
        todo = Todo.objects.get(pk=pk)
    except Todo.DoesNotExist:
        return JsonResponse({'error': 'Todo not found'}, status=404)
    
    if request.method == 'DELETE':
        todo.delete()
        return JsonResponse({'message': 'Todo deleted successfully'}, status=200)
    else:
        return HttpResponseNotAllowed(['DELETE'])