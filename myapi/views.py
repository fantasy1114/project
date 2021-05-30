# from rest_framework import viewsets

# from .serializers import HeroSerializer
# from .models import Hero


# class HeroViewSet(viewsets.ModelViewSet):
#     queryset = Hero.objects.all().order_by('name')
#     serializer_class = HeroSerializer

from joblib import PrintTime
from rest_framework import viewsets
from itsdangerous import Serializer
from matplotlib.pyplot import get
from rest_framework.response import Response
from yaml import serialize
from .models import Hero
from .serializers import HeroSerializer
from rest_framework.decorators import api_view
from django.core.mail import send_mail
from django.conf import settings
import time
@api_view(['GET'])
def heroList(request):
    time.sleep(0)
    heros = Hero.objects.all()
    serializer = HeroSerializer(heros, many=True)
    # print('=====>', serializer.data);
    return Response(serializer.data)

@api_view(['GET'])
def heroDetail(request, pk):
    heros = Hero.objects.get(id=pk)
    serializer = HeroSerializer(heros, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def heroCreate(request):
    serializer = HeroSerializer(data=request.data)
    try:
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    except Exception as e:
        print(e) 
        return Response("failed")

@api_view(['POST'])
def heroUpdate(request, pk):
    hero = Hero.objects.get(id=pk)
    serializer = HeroSerializer(instance=hero, data=request.data)

    if serializer.is_valid():
        serializer.save() 
    return Response(serializer.data)        

@api_view(['DELETE'])
def heroDelete(request, pk):
    hero = Hero.objects.get(id=pk)
    hero.delete()
    return Response ('Deleted')        

@api_view(['POST'])
def heroDeleteAll(request):
    del_contacts = request.data
    for item in del_contacts:
        Hero.objects.get(id=item).delete() 
    return Response("Deleted All")

@api_view(['POST'])
def heroSend(request):
    emailcontent = request.data
    email = emailcontent["data_email"]
    subject = emailcontent['data']['subject']
    content = emailcontent['data']['emailcontent']
    print(email)
    send_mail(subject, content, settings.EMAIL_HOST_USER, email)
    return Response("send")
    
    
    