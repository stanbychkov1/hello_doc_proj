from celery.result import AsyncResult
from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import URLmodel
from .serializers import URLSerializer, TagsSerializer, ResponseSerializer
from .tasks import num_apperances_of_tag


class URLViewSet(viewsets.ModelViewSet):
    queryset = URLmodel.objects.all()
    serializer_class = URLSerializer

    def retrieve(self, request, *args, **kwargs):
        res = AsyncResult(self.kwargs.get('pk'))
        if res.state == 'SUCCESS':
            if 'tags' in res.info:
                serializer = TagsSerializer(data=res.info)
            else:
                serializer = ResponseSerializer(data=res.info)
            serializer.is_valid(raise_exception=True)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_200_OK,
                            headers=headers)
        data = {'response': f'The task state is {res.state}'}
        serializer = ResponseSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK,
                        headers=headers)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        tags = num_apperances_of_tag.delay(serializer.data['url'])
        data = {'task_id': tags.task_id}
        headers = self.get_success_headers(serializer.data)
        return Response(data, status=status.HTTP_201_CREATED,
                        headers=headers)
