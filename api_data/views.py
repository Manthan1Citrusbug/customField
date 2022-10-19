from django.http import  JsonResponse
from rest_framework.views import APIView
from newfield.models import custom_field
from api_data.serializers import CustomFieldSerializer
from django.contrib.auth.models  import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class api_custom_field(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request,*args,**kwargs):
        try:
            user_data = User.objects.get(id = request.GET["id"])
        except:
            return JsonResponse("Something Wrong with ID", safe=False)
        cus_field_obj = custom_field.objects.filter(agent_id=user_data)
        serializer = CustomFieldSerializer(cus_field_obj, many=True)
        
        print(serializer.data)
        return JsonResponse(serializer.data, safe=False)