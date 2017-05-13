from django.contrib.auth import get_user_model
from rest_framework.exceptions import ValidationError

from rest_framework.serializers import (ModelSerializer,CharField)

User = get_user_model()

class UserCreateSerializer(ModelSerializer):
    password2 = CharField(label='Confirm Password')
    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'password2',
            'email',
        ]
        extra_kwargs = {
            'password' : {'write_only': True},
            'password2': {'write_only': True},
        }

    def validate_password(self, value):
        data = self.get_initial()
        password = data.get('password2')
        password2 = value
        if password != password2:
            raise ValidationError('Passwords must match')
        return value

    def validate_password2(self, value):
        data = self.get_initial()
        password = data.get('password')
        password2 = value
        if password != password2:
            raise ValidationError('Passwords must match')
        return value

    def create(self, validated_data):
        username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']
        user_obj = User(
            username=username,
            email=email
        )
        user_obj.set_password(password)
        user_obj.save()
        return validated_data

                         #OR
'''
    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
'''
                        #OR
'''
    from django.contrib.auth.hashers import make_password

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'],
            username=validated_data['username'],
            password=make_password(validated_data['password'])
        )
        user.save()
        return user
'''