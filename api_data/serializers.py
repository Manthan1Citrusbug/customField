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

    def create(self, validated_data):
        print(validated_data)
        cust_field = custom_field.objects.create(**validated_data)
        cust_field.agent_id = self.context['agent_id']
        cust_field.save()
        return cust_field


    def update(self, instance, validated_data):
        # instance is old data stored in database
        # validated data is new data you want to store in database
        instance.field_name = validated_data.get('field_name', instance.field_name)
        instance.field_type = validated_data.get('field_type', instance.field_type)
        instance.place_holder = validated_data.get('place_holder', instance.place_holder)
        instance.save()
        return instance

class FieldDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = field_data
        fields =  '__all__'
        read_only_fields = ['id']