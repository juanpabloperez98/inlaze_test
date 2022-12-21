from cerberus import Validator
from django.db import transaction
from django.db.models import Q
from django.shortcuts import render
from published.models import Published
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from users.models import User

from .serializers import PublishedSerializer, PublishedUserSerializer


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
        filters = (
            Q(user__pk=user.pk),
        )
        publishes = Published.objects.filter(*filters)
        #Make Serializer to show info
        published_data = PublishedSerializer(publishes, many = True).data
        return Response(
            data={
                "data": published_data
            },
            status=status.HTTP_200_OK,
        )

    
    @transaction.atomic(savepoint=True)
    def post(self, request):
        validator = Validator(
            schema={
                "title": {
                    "required": True,
                    "type": "string",
                },
                "comment": {
                    "required": True,
                    "type": "string",
                },
            },
        )
        if not validator.validate(document=request.data):
            return Response({
                "msg": validator.errors
            }, 
            status=status.HTTP_400_BAD_REQUEST
            )
        
        user = request.user
        to_add = validator.document
        to_add['user'] = user
        sid = transaction.savepoint()
        try:
            Published.objects.create(**to_add).pk
        except Exception as e:
            transaction.savepoint_rollback(sid)
            return Response({
                "msg": "User could not be created"
            }, status=status.HTTP_400_BAD_REQUEST)
        
        return Response({
            "msg": "Published created successfully"
        }, status=status.HTTP_200_OK)
        
    @transaction.atomic(savepoint=True)
    def put(self,request):
        validator = Validator(
            schema={
                "id": {
                    "required": True,
                    "type": "integer",
                },
                "title": {
                    "required": False,
                    "type": "string",
                },
                "comment": {
                    "required": False,
                    "type": "string",
                },
            },
        )
        if not validator.validate(document=request.data):
            return Response({
                "msg": validator.errors
            }, 
            status=status.HTTP_400_BAD_REQUEST
            )
        
        user = request.user
        if( not user ):
            return Response(data={
                "msg":"User Unathorizated"
            })

        filters = (
            Q(user__pk = user.pk),
            Q(id=validator.document.get("id")),
        )
        published = Published.objects.filter(*filters)
        if( not published ):
            return Response(data={
                "msg":"Published not found"
            },
            status=status.HTTP_404_NOT_FOUND
        )
        sid = transaction.savepoint()
        try:
            published.update(**validator.document)
        except Exception as e:
            print(e)
            transaction.savepoint_rollback(sid)
            return Response({
                "msg": "Published could not be updated"
            }, 
            status=status.HTTP_400_BAD_REQUEST
            )
        return Response({
            "msg": "Published updated successfully"
        }, status=status.HTTP_200_OK)

class PublishedAPI(APIView):
    
    def get(self,request):
        """
            Mehthod that returns published by user_id  
        """
        validator = Validator(
            schema={
                "user_id": {
                    "required": True,
                    "type": "string",
                },
            },
        )
        if not validator.validate(document=request.query_params):
            return Response({
                "msg": validator.errors
            }, 
            status=status.HTTP_400_BAD_REQUEST
            )
        filters = (
            Q(id=validator.document.get("user_id")),
        )
        user = User.objects.filter(*filters).first()
        if not user:
            return Response(data={
                "msg":"User Not found"
            },
            status=status.HTTP_404_NOT_FOUND
        )
        filters = (
            Q(user__pk=user.pk),
        )
        publishes = Published.objects.filter(*filters)
        published_data = PublishedUserSerializer(publishes, many = True).data
        return Response(
            data={
                "publishes": published_data
            },
            status=status.HTTP_200_OK,
        )
    


