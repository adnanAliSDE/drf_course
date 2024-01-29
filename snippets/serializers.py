from django.contrib.auth.models import User
from .models import Course
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    courses = serializers.HyperlinkedRelatedField(many=True, view_name="course-detail",read_only=True)

    class Meta:
        model = User
        fields = ["id", "username", "courses"]

class CourseSerializer(serializers.HyperlinkedModelSerializer):
    instructor = serializers.ReadOnlyField(source="owner.username")
    url = serializers.HyperlinkedIdentityField(view_name="course-detail")

    class Meta:
        model = Course
        fields = [
            "url",
            "title",
            "desc",
            "instructor",
            # "owner",
            "price",
        ]
