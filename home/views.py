from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View
from rest_framework.views import APIView
from rest_framework.response import Response
import os
from firebase_admin import credentials, firestore, initialize_app
import pdb
import pandas as pd
import firebase_admin
from firebase_admin import credentials
cred = credentials.Certificate('home/datakey.json')
default_app = initialize_app(cred)
db = firestore.client()

def data_table(self):
    todo_ref = db.collection('csvjson')
    all_todos = [doc.to_dict() for doc in todo_ref.stream()]
    data = pd.DataFrame(all_todos)
    return data
def bardf1990(self):
    data = data_table(1)  
    df1990 = data.loc[[0,7,52,94,111,126,183], "CounTries"]
    dff1990 =  data.loc[[0,7,52,94,111,126,183], "1990"]
    return list(df1990),list(dff1990)
def bardf1980(self):
    data = data_table(1)
    df1980 = data.loc[[0,7,52,94,111,126,183], "CounTries"]
    dff1980 =  data.loc[[0,7,52,94,111,126,183], "1980"]
    return list(df1980),list(dff1980)
def bardf2000(self):
    data = data_table(1)  
    df2000 = data.loc[[0,7,52,94,111,126,183], "CounTries"]
    dff2000 =  data.loc[[0,7,52,94,111,126,183], "2000"]
    return list(df2000),list(dff2000)
def bardf2010(self):
    data = data_table(1)
    df2010 = data.loc[[0,7,52,94,111,126,183], "CounTries"]
    dff2010 =  data.loc[[0,7,52,94,111,126,183], "2010"]
    return list(df2010),list(dff2010)
print(bardf2010(1))
# Create your views here.
User = get_user_model()
class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'bar_chart.html',{"customers": 10})


def get_data(request, *args, **kwargs):
    data = {
        "sales": 100, 
        "customers": 10,
    }
    return JsonResponse(data) # http response

class ChartData(APIView):
     authentication_classes = []
     permission_classes = []
     def get(self, request, format = None):
          data = {
               "sale": 100,
               "customers": 10,
               "user": User.objects.all().count()
          }
          return Response(data)

def index(request):
     return render(request, 'pages/base.html')
def data_analysis(request):
     return render(request, 'pages/data_analysis.html')
def simplechart(request):
     return render(request, 'pages/simplechart.html')
def base(request):
     return render(request, 'pages/base.html')
def home(request):
     return render(request, 'pages/home.html')
def bar_chart(request): 
     x1980,y1980 = bardf1980(1)
     x1990,y1990 = bardf1990(1)
     x2000,y2000 = bardf2000(1)
     x2010,y2010 = bardf2010(1)
     context=context={"x1980":x1980,'y1980':y1980,"x1990":x1990,'y1990':y1990,"x2000":x2000,'y2000':y2000,"x2010":x2010,'y2010':y2010}
     return render(request,'pages/bar_chart.html',context)
def line_chart(request):
     return render(request, 'pages/line_chart.html')
def scatter_chart(request):
     return render(request, 'pages/scatter_chart.html')
def pie_chart(request):
     x1980,y1980 = bardf1980(1)
     x1990,y1990 = bardf1990(1)
     x2000,y2000 = bardf2000(1)
     x2010,y2010 = bardf2010(1)
     context=context={"x1980":x1980,'y1980':y1980,"x1990":x1990,'y1990':y1990,"x2000":x2000,'y2000':y2000,"x2010":x2010,'y2010':y2010}
     return render(request,'pages/pie_chart.html',context)
def gant_chart(request):
     return render(request, 'pages/gant_chart.html')     
