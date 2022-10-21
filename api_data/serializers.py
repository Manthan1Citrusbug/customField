from asyncore import read
from rest_framework import serializers
from newfield.models import contact,custom_field,field_data




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
        fields =  ['custom_field_id','field_data']


class ContactSerializer(serializers.ModelSerializer):
    fields = FieldDataSerializer(many=True,read_only=False)
    class Meta:
        model = contact
        fields =  ['id',"phone_no","first_name","last_name","birthday","anniversary","tags","override_timezone","add_date","agent_id","fields"]
        read_only_fields = ['id','add_date']

    def create(self, validated_data):
        fields_data = validated_data.pop('fields')
        contact_data = contact.objects.create(**validated_data)
        contact_data.agent_id = self.context['agent_id']
        contact_data.save()
        for track_data in fields_data:
            field_data.objects.create(contact_id=contact_data, **track_data)
        return contact_data

    def update(self, instance, validated_data):
        # instance is old data stored in database
        # validated data is new data you want to store in database
        instance.phone_no = validated_data.get('phone_no', instance.phone_no)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.birthday = validated_data.get('birthday', instance.birthday)
        instance.anniversary = validated_data.get('anniversary', instance.anniversary)
        instance.tags = validated_data.get('tags', instance.tags)
        instance.override_timezone = validated_data.get('override_timezone', instance.override_timezone)
        instance.save()
        fields_data = validated_data.get('fields')
        print(fields_data)
        for item in fields_data:
            item_id = item.get('field_id')
            print(item_id)
            if item_id:
                inv_item = field_data.objects.get(id = item_id, contact_id = instance)
                print("INV ---- ",inv_item)
                inv_item.field_data = item.get('field_data', inv_item.field_data)
                inv_item.save()
            else:
                field_data.objects.create(contact_id=instance, **item)

        return instance