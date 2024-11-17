from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Blog



class UpdateUserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["id", "email", "username", "first_name", "last_name", "bio", "profile_picture",
                  "facebook", "youtube", "instagram", "twitter"]

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["id", "email", "username", "first_name", "last_name", "password"]
        extra_kwargs = {
            'password': {'write_only': True} 
        }
    
    def create(self, validated_data):
        email = validated_data["email"]
        username = validated_data["username"]
        first_name = validated_data["first_name"]
        last_name = validated_data["last_name"]
        first_name = validated_data["first_name"]
        password = validated_data["password"]

        user = get_user_model()
        new_user = user.objects.create(email=email, username=username, 
                                       first_name=first_name, last_name=last_name)
        new_user.set_password(password)
        new_user.save()
        return new_user

class SimpleAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["id", "username", "first_name", "last_name", "profile_picture"]

class BlogSerializer(serializers.ModelSerializer):
    author = SimpleAuthorSerializer(read_only=True)
    class Meta:
        model = Blog
        fields = ['id', 'title', 'slug', 'author', 'category', 'content', 'featured_image', 'published_date', 'created_at', 'updated_at', 'is_draft']

        