# MODEL AND SERIALIZERS IMPORT
from api_data.serializers import ContactSerializer, CustomFieldSerializer
from newfield.models import contact, custom_field
from django.contrib.auth.models import User

# REST FRAMEWORK IMPORTS
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

# API Class for Custom Field Add, Update, View


class api_custom_field(ListAPIView):
    # check for authentication and authorization
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = PageNumberPagination

    # Send all data in the response
    def get(self, request):
        try:
            cus_field_obj = custom_field.objects.filter(agent_id=request.user)
            page = self.paginate_queryset(cus_field_obj)
            if page is not None:
                serializer = CustomFieldSerializer(page, many=True)
                # send success response
                return self.get_paginated_response(serializer.data)
        except:
            # send error massage
            return Response("No Data Found", status=status.HTTP_204_NO_CONTENT)

    # create new custom field from api data

    def post(self, request):
        serializer = CustomFieldSerializer(data=request.data, context={
                                           'agent_id': request.user})
        if serializer.is_valid():
            print(serializer.validated_data)
            created_data = serializer.save()
            # send success response
            return Response(
                {
                    'Field Name': created_data.field_name,
                    'Type': created_data.field_type,
                    'Placeholder': created_data.place_holder,
                    'Created on': created_data.add_date,
                    'Agent ID': created_data.agent_id.id
                },
                status=status.HTTP_201_CREATED
            )
        # send error massage
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # update full and partial data of the custom field
    def put(self, request):
        try:
            custom_field_obj = custom_field.objects.get(
                id=request.data["id"], agent_id=request.user)
            serializer = CustomFieldSerializer(
                custom_field_obj, data=request.data, partial=True)
            if serializer.is_valid():
                print(serializer.validated_data)
                created_data = serializer.save()
                # send success response
                return Response(
                    {
                        'Field Name': created_data.field_name,
                        'Type': created_data.field_type,
                        'Placeholder': created_data.place_holder,
                        'Created on': created_data.add_date,
                        'Agent ID': created_data.agent_id.id
                    },
                    status=status.HTTP_200_OK
                )
            # send error massage
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except custom_field.DoesNotExist:
            return Response({'error': "No Data Found"}, status=status.HTTP_204_NO_CONTENT)


class api_contact(ListAPIView):
    # check for authentication and authorization
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = PageNumberPagination
    filter_backends = [SearchFilter, ]
    search_fields = ('first_name', 'last_name')
    # Send all data in the response

    def get(self, request):
        try:
            cus_field_obj = self.filter_queryset(
                contact.objects.filter(agent_id=request.user))
        except:
            # send error massage
            return Response("No Data Found", status=status.HTTP_204_NO_CONTENT)
        page = self.paginate_queryset(cus_field_obj)
        if page is not None:
            serializer = ContactSerializer(page, many=True)

            # send success response
            return self.get_paginated_response(serializer.data)
        
        # send error massage
        return Response("No Data Found", status=status.HTTP_204_NO_CONTENT)

    # create new Contact field from api data
    def post(self, request):
        print(request.data)
        serializer = ContactSerializer(data=request.data, context={'agent_id': request.user})
        if serializer.is_valid():
            serializer.save()

            # send success response
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        # send error massage
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # update full and partial data of the Contact Model
    def put(self, request):
        print(request.data)
        try:
            contact_obj = contact.objects.get(id = request.data["id"], agent_id = request.user)
        except contact.DoesNotExist:
            return Response({'error':"No Data Found"},status = status.HTTP_204_NO_CONTENT)

        serializer = ContactSerializer(contact_obj, data = request.data, partial = True )
        if serializer.is_valid():
            print(serializer.validated_data)
            serializer.save()

            # send success response
            return Response(
                serializer.data,
                status = status.HTTP_200_OK
            )
        # send error massage
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        try:
            contact_obj = contact.objects.get(id=request.data["id"])
            contact_obj.delete()

            # send success response
            return Response("Data Successfully Deleted", status=status.HTTP_204_NO_CONTENT)
        except:
            # send error massage
            return Response("No Data Found", status=status.HTTP_204_NO_CONTENT)


