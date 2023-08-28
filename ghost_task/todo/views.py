from rest_framework.response import Response
from rest_framework.views import APIView
from todo.models import Todo, Status
import datetime
from todo.serializer import TodoSerializer, StatusSerializer


class TodoList(APIView):
    serializer_class = TodoSerializer

    def get(self, request):
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TodoSerializer(data=request.data)        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)        
        return Response('Validation error', status=400)


class TodoView(APIView):
    serializer_class = TodoSerializer

    def get(self, request, id):
        try:
            todo = Todo.objects.get(id=id)
            serializer = TodoSerializer(todo)
            return Response(serializer.data, status=200)
        except Exception as e:
            return Response(str(e), status=404)

    def put(self, request, id):
        field = request.data['field']
        value = request.data['value']        
        if not value:
            value = None

        try:
            Todo.objects.filter(id=id).update(
                **{field: value},
            )
        except Todo.DoesNotExist:
            return Response({}, status=404)
        return Response('ok', status=200)

    def patch(self, request, id):
        try:
            todo = Todo.objects.get(id=id)
        except Exception as e:
            return Response(e, status=404)

        row_id = request.data.get('row_id')
        if row_id:
            Todo.objects.filter(id=id).update(status=row_id)
            return Response('success', status=200)

        title = request.data.get('title')
        status = request.data.get('status')
        text = request.data.get('text')

        if title is not None:
            todo.title = title
        if status is not None:
            todo.status = status
        if text is not None:
            todo.text = text

        todo.save()

        serializer = TodoSerializer(todo)
        return Response(serializer.data, status=200)

    def delete(self, request, id):
        try:
            Todo.objects.get(id=id).delete()
        except Exception as e:
            return Response(e, status=404)
        return Response('ok', status=200)


class StatusList(APIView):
    serializer_class = StatusSerializer

    def get(self, request):
        status = Status.objects.all()
        serializer = StatusSerializer(status, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StatusSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)


class StatusView(APIView):
    serializer_class = StatusSerializer

    def get(self, request, id):
        try:
            status = Status.objects.get(id=id)
            return Response(StatusSerializer(status).data, status=200)
        except Exception as e:
            return Response(str(e), status=404)

    def patch(self, request, id):
        try:
            status_obj = Status.objects.get(id=id)
        except Exception as e:
            return Response(e, status=404)

        status = request.data.get('status')

        if status is not None:
            status.status = status

        status_obj.save()

        serializer = StatusSerializer(status_obj)
        return Response(serializer.data, status=200)

    def delete(self, request, id):
        try:
            Status.objects.get(id=id).delete()
        except Exception as e:
            return Response(e, status=404)
        return Response('ok', status=200)
