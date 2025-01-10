from rest_framework import generics as views, status
from rest_framework.response import Response

class HelloAuthView(views.GenericAPIView):
    def get(self, request):
        return Response(
            data={
                'message': 'Hello !'
            },
            status=status.HTTP_200_OK,
        )
