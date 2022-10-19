from rest_framework import serializers
from newfield.models import contact,custom_field,field_data


class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = contact
        fields =  '__all__'
        read_only_fields = ['id','add_date']


class CustomFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = custom_field
        fields =  '__all__'
        read_only_fields = ['id','add_date']

class FieldDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = field_data
        fields =  '__all__'
        read_only_fields = ['id']