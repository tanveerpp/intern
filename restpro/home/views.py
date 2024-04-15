from django.shortcuts import render
import requests
def useapi(request):
    #data=requests.get('https://mejevo.pythonanywhere.com/emps/')
    data=requests.get('http://127.0.0.1:8000/customer/')
    d=data.json()
    for i in d:
        #print(i['product'])
        p=requests.get(i['product'])
        #print(p.json())
        i['product']=p.json()
    print(d)
    return render(request,'index.html',{'data':d})
