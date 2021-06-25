from django.shortcuts import render
import random
from .models import *
from django.core.mail import send_mail
from .utils import *
from django.http import HttpResponseRedirect
from django.urls.base import reverse
from secretary.models import *
import datetime

# Create your views here.

def watchman_home(request):
    if "email" in request.session:
        uid = User.objects.get(email=request.session['email'])

        if uid.role == "Watchman":
            wid = Watchman.objects.get(user_id=uid)
            user_id = User.objects.get(role="Chairman")

            cid = Chairman.objects.get(user_id=user_id) 

            return render(request,"secretary/dashboard/watchman-index.html",{'uid':uid,'wid':wid,'cid':cid})
     
    return render(request,"secretary/login.html")

# def send_request(request,p_pk,d_pk):
#     watchman_id = Watchman.objects.get(id=p_pk)
#     chairman_id = Chairman.objects.get(id=d_pk)    
#     cid = ClientRequest.objects.create(watchman_id=watchman_id,chairman_id=chairman_id)

#     return HttpResponseRedirect(reverse('patient:all-doctors'))

