from rest_framework import serializers
from . models import *

class MemberCommunicationTypeSerializeres(serializers.ModelSerializer):
      class Meta :
        model= MemberCommunicationType
        fields= '__all__'
       # fields =['name','city','roll']