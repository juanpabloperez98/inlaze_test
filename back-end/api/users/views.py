from cerberus import Validator
from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login
from django.db import transaction
from django.db.models import Q
from django.shortcuts import render
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User

# Create your views here.


class RegisterUser(APIView):

    @transaction.atomic(savepoint=True)
    def post(self, request):
        """
        Sing up a new user in platform
        """
        validator = Validator(
            schema={
                "nickname": {
                    "required": True,
                    "type": "string",
                },
                "names": {
                    "required": True,
                    "type": "string",
                },
                "lastname": {
                    "required": True,
                    "type": "string",
                },
                "email": {
                    "required": True,
                    "type": "string",
                },
                "password": {
                    "required": True,
                    "type": "string",
                },
            },
        )

        if not validator.validate(
            document=request.data,
            normalize=False,
        ):
            return Response(
                {
                    "msg": validator.errors
                }, status=status.HTTP_400_BAD_REQUEST
            )

        filters = (
            Q(
                email=validator.document.get("email"),
            ),
        )
        user = User.objects.filter(*filters).first()

        if (user):
            return Response(
                data={
                    "msg": "Email Already used"
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        sid = transaction.savepoint()
        try:
            user = User.objects.create_user(**validator.document)
        except Exception as e:
            transaction.savepoint_rollback(sid)
            return Response({
                "msg": "User could not be created"
            }, status=status.HTTP_400_BAD_REQUEST)

        return Response({
            "msg": "User created successfully"
        }, status=status.HTTP_200_OK)


class Login(APIView):

    @transaction.atomic(savepoint=True)
    def post(self, request):
        validator = Validator(
            schema={
                "email": {
                    "required": True,
                    "type": "string",
                },
                "password": {
                    "required": True,
                    "type": "string",
                },
            },
        )
        if not validator.validate(
            document=request.data,
            normalize=False,
        ):
            return Response({
                "msg": validator.errors
            }, status=status.HTTP_400_BAD_REQUEST)


        user = authenticate(
            username=request.data.get("email"),
            password=request.data.get("password"),
        )

        if user is None:
            return Response(
                data={
                    "msg": "There is not such user or the password is invalid",
                },
                status=status.HTTP_404_NOT_FOUND,
            )
        sid = transaction.savepoint()
        try:
            update_last_login(None, user)
            token = Token.objects.update_or_create(
                user=user,
                defaults={
                    "user": user,
                },
            )[0]
            transaction.savepoint_commit(sid=sid)
            return Response(
                data={
                    "token": token.key
                },
                status=status.HTTP_200_OK,
            )
        except Exception as e:
            print(e)
            transaction.savepoint_rollback(sid)
            return Response({
                "msg": "User could not be created"
            }, status=status.HTTP_400_BAD_REQUEST)




