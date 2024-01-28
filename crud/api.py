from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from .serializer import INFOSerializer
from .models import INFOList

class Api(GenericAPIView):
    def delete(self, request, pk):
        try:
            obj = INFOList.objects.get(email=pk)
            obj.delete()
            return Response(status=200, data={'message': 'Deleted Successfully!'})
        except Exception as e:
            return Response(status=400, data={"Error": e})

    def patch(self, request, pk):
        name = request.data['name']
        phone = request.data['phone']
        if name and phone:
            try:
                obj = INFOList.objects.get(email=pk)
                obj.name = name
                obj.phone = phone
                obj.save()
                return Response(status=200, data={'message': 'Changed Successfully!'})
            except Exception as e:
                return Response(status=400, data={"Error": e})
        
    def get(self, request, pk=None):
        if pk:
            obj = INFOList.objects.get(email=pk)
            sl_obj = INFOSerializer(obj)
            return Response(status=200,data= sl_obj.data)
        else:
            obj = INFOList.objects.filter().all()
            sl_obj = INFOSerializer(obj, many=True)
            return Response(status=200,data= sl_obj.data)
