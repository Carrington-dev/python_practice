from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from scope_app.models import Dino
from rest_framework import mixins
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, schema
from scope_app.serializer import DinoSerializer

# Create your views here.
class DinoViewSets(ModelViewSet):
    serializer_class = DinoSerializer
    queryset = Dino.objects.all()

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    @api_view(['GET','DELETE', 'UPDATE'])
    def dino_detail(self, pk):
        if self.request == "DELETE":
            dino = Dino.objects.get(pk)
            dino.delete()
        
            return Response(status=status.HTTP_204_NO_CONTENT)


# class ZoneLocationViewSet(generics.UpdateAPIView, ModelViewSet):
#     serializer_class = ZoneUpdateSerializer
#     # queryset = Dino.objects.all()

#     def get_queryset(self):
#         return super().get_queryset()

#     def post(self, request):
#         serializer = ZoneUpdateSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)



