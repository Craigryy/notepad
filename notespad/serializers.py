''' Script to serialize and handle the conversion between python objects and JSON format.'''

from rest_framework import serializers
from .models import Page,Note

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields='__all__'


class PageSerializer(serializers.ModelSerializer):
    note = NoteSerializer()
    class Meta:
        model = Page
        fields ='__all__'