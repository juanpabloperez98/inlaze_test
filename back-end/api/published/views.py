from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from users.models import User

from published.models import Published


class PublishedByUserSession(APIView):

    permission_classes = [
        IsAuthenticated,
    ]
    def get(self, request):
        """
            Return messages from user actived
        """
        user = request.user
        if( not user ):
            return Response(data={
                "msg":"User Unathorizated"
            })
        
        print(user)
        

        return Response(
            data={
                "msg": "ok"
            },
            status=status.HTTP_200_OK,
        )


