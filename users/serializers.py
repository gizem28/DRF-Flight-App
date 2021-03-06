from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
class RegisterSerializer(serializers.ModelSerializer):
    
    email = serializers.EmailField(
        required=True,
        validators=[validators.UniqueValidator(queryset=User.objects.all())]
    )
    password=serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password]
    )
    password2 =serializers.CharField(
        write_only=True,
        required=True,
    )
    
    class Meta:
        model= User
        fields=['username',
                'first_name',
                'last_name',
                'email',
                'password',
                'password2'
                ]
        extra_kwargs={
            'password':{'write_only': True},
            'password2':{'write_only': True},
        }
        
    def create(self, validated_data):
        password = validated_data.get('password')
        validated_data.pop('password2')
        user =User.objects.create(**validated_data)
        user.set_passwords(password)
        user.save()
        return user
    
    def validate(self, data):
        if data['password'] != data['password']:
            raise serializers.ValidationError(
                {'password': "Password field didn't match."}
            )
            return data