from django.shortcuts import render    
import random
from .models import *
from django.core.mail import send_mail
from .utils import *
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from members.models import *
import pyttsx3
import PyPDF2





# Create your views here.


def home(request): 
    if "email" in request.session:
        uid = User.objects.get(email=request.session['email'])

        if uid.role == "Chairman":
             
            cid = Chairman.objects.get(user_id=uid)    
            nall = NoticeBoard.objects.all()
            nlis = NoticeBoard.objects.all().count()
            mall = Members.objects.all().count()
            ec = Events.objects.all().count()
            eall = Events.objects.all()
            speaker = pyttsx3.init()
            speaker.say('how are you Chairman Welcome to Digital Society')
            speaker.runAndWait()
            print("----->notice",nall)
            return render(request,"secretary/dashboard/index.html",{'speaker':speaker,'eall':eall,'ec':str(ec),'nall':nall,'uid':uid,'cid':cid,'nlis':str(nlis),'mall':str(mall)})
         
    return render(request,"secretary/login.html")

def mem(request):
    if "email" in request.session:
        uid = User.objects.get(email=request.session['email'])

        if uid.role == "Members":
            mid = Members.objects.get(user_id=uid)
            user_id = User.objects.get(role="Chairman")
            cid = Chairman.objects.get(user_id=user_id) 
            nall = NoticeBoard.objects.all()
            nlis = NoticeBoard.objects.all().count()
            mall = Members.objects.all().count()
            ec = Events.objects.all().count()
            eall = Events.objects.all()
            print("----->notice",nall)

            cid = Chairman.objects.get(user_id=user_id) 

            return render(request,"secretary/dashboard/members-index.html",{'eall':eall,'ec':str(ec),'nall':nall,'uid':uid,'mid':mid,'cid':cid,'nlis':str(nlis),'mall':str(mall)})
     
    return render(request,"secretary/login.html")

def watchman_home(request):
    if "email" in request.session:
        uid = User.objects.get(email=request.session['email'])

        if uid.role == "Watchman":
            wid = Watchman.objects.get(user_id=uid)
            user_id = User.objects.get(role="Chairman")
            cid = Chairman.objects.get(user_id=user_id) 
            nall = NoticeBoard.objects.all()
            nlis = NoticeBoard.objects.all().count()
            mall = Members.objects.all().count()
            ec = Events.objects.all().count()
            eall = Events.objects.all()
            print("----->notice",nall)
            return render(request,"secretary/dashboard/watchman-index.html",{'eall':eall,'ec':str(ec),'nall':nall,'uid':uid,'wid':wid,'cid':cid,'nlis':str(nlis),'mall':str(mall)})
     
    return render(request,"secretary/login.html")
      


def login(request):
    if "email" in request.session:
        uid = User.objects.get(email=request.session['email'])
        if uid.role == "Chairman":
            cid = Chairman.objects.get(user_id=uid)
            nall = NoticeBoard.objects.all()
            nlis = NoticeBoard.objects.all().count()
            mall = Members.objects.all().count()
            ec = Events.objects.all().count()
            eall = Events.objects.all()
            print("----->notice",nall)
            return render(request,"secretary/dashboard/index.html",{'cid':cid,'eall':eall,'nall':nall,'uid':uid,'nlis':str(nlis),'mall':str(mall),'ec':str(ec)})
        elif uid.role == "Members":
            mid = Members.objects.get(user_id=uid)
            nall = NoticeBoard.objects.all()
            nlis = NoticeBoard.objects.all().count()
            mall = Members.objects.all().count()
            ec = Events.objects.all().count()
            eall = Events.objects.all()
            print("----->notice",nall)
            return render(request,"secretary/dashboard/members-index.html",{'eall':eall,'nall':nall,'uid':uid,'mid':mid,'nlis':str(nlis),'mall':str(mall),'ec':str(ec)})
        elif uid.role == "Watchman":
            wid = Watchman.objects.get(user_id=uid)
            nall = NoticeBoard.objects.all()
            nlis = NoticeBoard.objects.all().count()
            mall = Members.objects.all().count()
            ec = Events.objects.all().count()
            eall = Events.objects.all()
            print("----->notice",nall)
            return render(request,"secretary/dashboard/watchman-index.html",{'eall':eall,'nall':nall,'uid':uid,'wid':wid,'nlis':str(nlis),'mall':str(mall),'ec':str(ec)})
        
    else:
        if request.POST:
            uid = User.objects.get(email=request.POST['email'])
            if uid.password == request.POST['password']:
                print("Role---",uid.role)
                if uid.role == 'Chairman':
                    
                    cid = Chairman.objects.get(user_id=uid)
                    nlis = NoticeBoard.objects.all().count()
                    mall = Members.objects.all().count()
                    ec = Events.objects.all().count()
                    eall = Events.objects.all()
                    nall = NoticeBoard.objects.all()
                    eall = Events.objects.all()

                    if uid.is_verfied: 
                        request.session['email'] = uid.email
                        return render(request,"secretary/dashboard/index.html",{'eall':eall,'nall':nall,'uid':uid,'cid':cid,'nlis':str(nlis),'mall':str(mall),'ec':str(ec)})
                    else : 
                        return render(request,"secretary/resetpassword.html",{'email': uid.email})
                        
                elif uid.role == 'Members': 
                    #patients login code

                    mid = Members.objects.get(user_id=uid)
                    user_id=User.objects.get(role="Chairman")
                    print("-->",user_id)
                    cid = Chairman.objects.get(user_id=user_id)
                    print("--->",cid.address)
                    nall = NoticeBoard.objects.all()
                    eall = Events.objects.all()
                    nlis = NoticeBoard.objects.all().count()
                    mall = Members.objects.all().count()
                    ec = Events.objects.all().count()
                    eall = Events.objects.all()
                    nall = NoticeBoard.objects.all()
                
                    
                    print("----->notice",nall)
                    if uid.is_verfied: 
                        request.session['email'] = uid.email
                        return render(request,"secretary/dashboard/members-index.html",{'eall':eall,'nall':nall,'uid':uid,'mid':mid,'cid':cid,'nlis':str(nlis),'mall':str(mall),'ec':str(ec)})
                    else : 
                        return render(request,"secretary/resetpassword.html",{'email': uid.email})
                
                elif uid.role == 'Watchman': 
                    #patients login code
                    
                    wid = Watchman.objects.get(user_id=uid)
                    print("Firstname--",wid.firstname)
                    user_id=User.objects.get(role="Chairman")
                    print("-->",user_id)
                    cid = Chairman.objects.get(user_id=user_id)
                    print("--->",cid.address)
                    print("WATCHMAN")
                    nall = NoticeBoard.objects.all()
                    eall = Events.objects.all()
                    nlis = NoticeBoard.objects.all().count()
                    mall = Members.objects.all().count()
                    ec = Events.objects.all().count()
                    eall = Events.objects.all()
                    nall = NoticeBoard.objects.all()
                    print("----->notice",nall)
                    if uid.is_verfied: 
                        request.session['email'] = uid.email
                        return render(request,"secretary/dashboard/watchman-index.html",{'eall':eall,'nall':nall,'uid':uid,'wid':wid,'cid':cid,'nlis':str(nlis),'mall':str(mall),'ec':str(ec)})
                    else : 
                        return render(request,"secretary/resetpassword.html",{'email': uid.email})
                        
            else:
                e_msg = "Invalid password"
                return render(request,"secretary/login.html",{'e_msg':e_msg})

        return render(request,"secretary/login.html")
   
def register(request):
    try:
        if request.POST:
            firstname = request.POST['firstname']
            email = request.POST['email']
            contact = request.POST['contact']
            role = request.POST['role']

            li = ["65","55","98","74","62","32","54"]
            ch = random.choice(li)
            password = firstname[1:]+email[3:6]+ch

            print("----------> password",password)
        
            if role == "Chairman":
                uid = User.objects.create(email=email,password=password,role=role)
                cid = Chairman.objects.create(user_id=uid,firstname=firstname,contact=contact)

                subject = "WELCOME TO Digital-Society"
                
                # send_mail(subject,message,from_email,[email])
                sendmail(subject,'maintemplate',email,{'firstname': firstname ,'password' : password})
                return render(request,"secretary/login.html")

            elif role == "Members":
                # patient coding
                uid = User.objects.create(email=email,password=password,role=role)
                mid = Members.objects.create(user_id=uid,firstname=firstname,contact=contact)

                subject = "WELCOME TO Digital-Society"
                
                # send_mail(subject,message,from_email,[email])
                sendmail(subject,'members_maintemplate',email,{'firstname': firstname})
                return render(request,"secretary/login.html")

            elif role == "Watchman":
                # patient coding
                uid = User.objects.create(email=email,password=password,role=role)
                wid = Watchman.objects.create(user_id=uid,firstname=firstname,contact=contact)

                subject = "WELCOME TO Digital-Society"
                
                # send_mail(subject,message,from_email,[email])
                sendmail(subject,'watchman_maintemplate',email,{'firstname': firstname})
                return render(request,"secretary/login.html")
        else:
            return render(request,"secretary/register.html")
    except:
        e_msg = "Something went wrong"
        return render(request,"secretary/register.html",{'e_msg':e_msg})

def reset_password(request):
    if request.POST:
        email = request.POST['email']
        password = request.POST['password']
        newpassword = request.POST['newpassword']
        repassword = request.POST['repassword']
        uid = User.objects.get(email=email)
        if uid.is_verfied:
            pass
        else:
            if uid.password == password and newpassword == repassword:
                uid.password = newpassword   # set your new password
                uid.is_verfied = True
                uid.save()     # update
                #s_msg ="Your password is sucessfully reset"
                messages.info(request, "You have sucessfully login and yor password is reset")
                return render(request,"secretary/login.html")
                #return HttpResponseRedirect(reverse('login'))
            elif newpassword != repassword:
                p_msg = "Password doesn't match"
                return render(request,"secretary/resetpassword.html",{'email':uid.email,'p_msg':p_msg})
    else:
        return render(request,"secretary/resetpassword.html")

def logout(request):
    if "email" in request.session:
        del request.session['email']
        return render(request,"secretary/login.html")
    else:
        return render(request,"secretary/login.html")

def myprofile(request):
    uid = User.objects.get(email = request.session['email'])
    cid = Chairman.objects.get(user_id=uid)  
    return render(request,'secretary/dashboard/profile.html',{'uid':uid,'cid':cid})


def resetprofile(request):
    uid = User.objects.get(email = request.session['email'])
    cid = Chairman.objects.get(user_id=uid)

    if request.POST:
        cid.firstname = request.POST['firstname']
        cid.lastname = request.POST['lastname']
        cid.country = request.POST['country']
        cid.state = request.POST['state']
        cid.city = request.POST['city']
        cid.contact = request.POST['contact']
        cid.address = request.POST['age']
        cid.gender = request.POST['gender']
        cid.address = request.POST['address']
        cid.aboutme = request.POST['aboutme']
        cid.work = request.POST['work']
        cid.age = request.POST['age']
        
        if request.FILES:
            cid.profile_pic = request.FILES['profile']

        cid.save()
    return render(request,'secretary/dashboard/profile.html',{'uid':uid,'cid':cid})

def reset_profile_password(request):
    uid = User.objects.get(email = request.session['email'])
    cid = Chairman.objects.get(user_id=uid)

    currentpassword = request.POST['currentpassword']
    newpassword = request.POST['newpassword']

    if uid.password == currentpassword:
        uid.password = newpassword
        uid.save()
    else:
        msg = "Invalid Password"
    return render(request,'secretary/dashboard/profile.html',{'uid':uid,'cid':cid})

def memberprofile(request):
    uid = User.objects.get(email = request.session['email'])
    mid = Members.objects.get(user_id=uid)  
    user_id = User.objects.get(role="Chairman")
    cid = Chairman.objects.get(user_id=user_id)

    return render(request,'secretary/dashboard/memprofile.html',{'uid':uid,'mid':mid,'cid':cid})

def watchmanprofile(request):
    uid = User.objects.get(email = request.session['email'])
    wid = Watchman.objects.get(user_id=uid)  
    user_id = User.objects.get(role="Chairman")
    cid = Chairman.objects.get(user_id=user_id)

    return render(request,'secretary/dashboard/watchman_profile.html',{'uid':uid,'wid':wid,'cid':cid})

def memberresetprofile(request):
    uid = User.objects.get(email = request.session['email'])
    mid = Members.objects.get(user_id=uid)

    if request.POST:
        mid.firstname = request.POST['firstname']
        mid.lastname = request.POST['lastname']
        mid.country = request.POST['country']
        mid.state = request.POST['state']
        mid.city = request.POST['city']
        mid.contact = request.POST['contact']
        mid.address = request.POST['age']
        mid.gender = request.POST['gender']
        mid.address = request.POST['address']
        mid.aboutme = request.POST['aboutme']
        mid.work = request.POST['work']
        mid.age = request.POST['age']
        mid.blood_grp = request.POST['blood_grp']
        mid.birthdate = request.POST['birthdate']
        # mid.job_address = request.POST['job_address']
        mid.vechicle_deatails = request.POST['vechicle_deatails']
        mid.marrial_status = request.POST['marrial_status']
        mid.house_no = request.POST['house_no']
        mid.family_members = request.POST['family_members']
        mid.o_r = request.POST['o_r']
        
        if request.FILES:
            mid.profile_pic = request.FILES['profile']

        mid.save()
    return render(request,'secretary/dashboard/memprofile.html',{'uid':uid,'mid':mid})

def watchmanresetprofile(request):
    uid = User.objects.get(email = request.session['email'])
    wid = Watchman.objects.get(user_id=uid)

    if request.POST:
        wid.firstname = request.POST['firstname']
        wid.lastname = request.POST['lastname']
        wid.country = request.POST['country']
        wid.state = request.POST['state']
        wid.city = request.POST['city']
        wid.contact = request.POST['contact']
        wid.address = request.POST['age']
        wid.gender = request.POST['gender']
        wid.address = request.POST['address']
        wid.aboutme = request.POST['aboutme']
        wid.work = request.POST['work']
        wid.age = request.POST['age']
        wid.blood_grp = request.POST['blood_grp']
        wid.birthdate = request.POST['birthdate']
        wid.vechicle_deatails = request.POST['vechicle_deatails']
        wid.marrial_status = request.POST['marrial_status']
        
        if request.FILES:
            wid.profile_pic = request.FILES['profile']

        wid.save()
    return render(request,'secretary/dashboard/watchman_profile.html',{'uid':uid,'wid':wid})


def memberreset_profile_password(request):
    uid = User.objects.get(email = request.session['email'])
    mid = Members.objects.get(user_id=uid)

    currentpassword = request.POST['currentpassword']
    newpassword = request.POST['newpassword']

    if uid.password == currentpassword:
        uid.password = newpassword
        uid.save()
    else:
        msg = "Invalid Password"
    return render(request,'secretary/dashboard/memprofile.html',{'uid':uid,'mid':mid})

def watchmanreset_profile_password(request):
    uid = User.objects.get(email = request.session['email'])
    wid = Watchman.objects.get(user_id=uid)

    currentpassword = request.POST['currentpassword']
    newpassword = request.POST['newpassword']

    if uid.password == currentpassword:
        uid.password = newpassword
        uid.save()
    else:
        msg = "Invalid Password"
    return render(request,'secretary/dashboard/watchman_profile.html',{'uid':uid,'wid':wid})


def allmembers(request):
    uid = User.objects.get(email = request.session['email'])
    user_id = User.objects.get(role="Chairman")

    cid = Chairman.objects.get(user_id=user_id) 
    mid = Members.objects.get(user_id=uid)


    mall = Members.objects.exclude(user_id=uid) # retrive all data from the model

    # dall = Doctor.objects.all()  
    return render(request,'secretary/dashboard/Allmembers.html',{'uid':uid,'mid':mid,'mall':mall,cid:'cid'})

def watchman_all_members(request):
    uid = User.objects.get(email = request.session['email'])
    user_id=User.objects.get(role="Chairman")
    print("-->",user_id)
    cid = Chairman.objects.get(user_id=user_id)
    wid = Watchman.objects.get(user_id=uid)
    mall = Members.objects.exclude(user_id=uid) # retrive all data from the model

    # dall = Doctor.objects.all()  
    return render(request,'secretary/dashboard/watchman_all_member.html',{'uid':uid,'wid':wid,'mall':mall,cid:'cid'})

def allmember(request):
    uid = User.objects.get(email = request.session['email'])
    cid = Chairman.objects.get(user_id=uid)

    mall = Members.objects.exclude(user_id=uid) # retrive all data from the model

    # dall = Doctor.objects.all()  
    return render(request,'secretary/dashboard/Allmember.html',{'uid':uid,'cid':cid,'mall':mall})

def view_profile(request,pk):
    memberid = Members.objects.get(id = pk)  # for respective selected user
    uid = User.objects.get(email = request.session['email'])  # for logged in
    mid = Members.objects.get(user_id=uid)
    return render(request,'secretary/dashboard/view-profile.html',{'uid':uid,'memberid':memberid,'mid':mid})

def watchman_can_see_member_view_profile(request,pk):
    memberid = Members.objects.get(id = pk)  # for respective selected user
    uid = User.objects.get(email = request.session['email'])  # for logged in
    # mid = Members.objects.get(user_id=uid)
    wid = Watchman.objects.get(user_id=uid)
    return render(request,'secretary/dashboard/watchman_can_see_member_view_profile.html',{'uid':uid,'memberid':memberid,'wid':wid})

def c_view_memprofile(request,pk):
    memberid = Members.objects.get(id = pk)  # for respective selected user
    uid = User.objects.get(email = request.session['email'])  # for logged in
    # mid = Members.objects.get(user_id=uid)
    cid = Chairman.objects.get(user_id=uid)
    return render(request,'secretary/dashboard/c-view-memprofile.html',{'uid':uid,'memberid':memberid,'cid':cid})

def watchman_request(request):
    uid = User.objects.get(email = request.session['email'])
    cid = Chairman.objects.get(user_id=uid)
    wid = Watchman.objects.all()
    
    return render(request,'secretary/dashboard/watchman_request.html',{'uid':uid,'cid':cid,'wid':wid})

def members_request(request):
    uid = User.objects.get(email = request.session['email'])
    cid = Chairman.objects.get(user_id=uid)
    mid = Members.objects.all()
    
    return render(request,'secretary/dashboard/members_request.html',{'uid':uid,'cid':cid,'mid':mid})

def watchman_status(request,pk,status):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        wid=Watchman.objects.get(id=pk)
        cid=Chairman.objects.get(user_id=uid)
        wid.status=status
        wid.save()
        if wid.status=="Approved":
            li = ["65","55","98","74","62","32","54"]
            ch = random.choice(li)
            password = wid.firstname[1:]+ch
            wuid=User.objects.get(id=wid.user_id.id)
            wuid.password = password
            wuid.save()
            uid.save()
            
            subject = "WELCOME TO Digital-Society"
                
            # send_mail(subject,message,from_email,[email])
            
            sendmail(subject,"watchman_req_maintemplate",wuid.email,{"wid":wid,"status":status,'password':password})
        wid = Watchman.objects.all()
     
        return render(request,"secretary/dashboard/watchman_request.html",{'uid':uid,'wid':wid,'cid':cid})
    else:
        return render(request,"secretary/login.html")

def members_status(request,pk,status):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        mid=Members.objects.get(id=pk)
        cid=Chairman.objects.get(user_id=uid)
        mid.status=status
        mid.save()
        if mid.status=="Approved":
            li = ["65","55","98","74","62","32","54"]
            ch = random.choice(li)
            password = mid.firstname[1:]+ch
            muid=User.objects.get(id=mid.user_id.id)
            muid.password = password
            muid.save()
            uid.save()
            
            subject = "WELCOME TO Digital-Society"
                
            # send_mail(subject,message,from_email,[email])
            
            sendmail(subject,"maintemplate",muid.email,{"mid":mid,"status":status,'password':password})
        mid = Members.objects.all()
     
        return render(request,"secretary/dashboard/members_request.html",{'uid':uid,'mid':mid,'cid':cid})
    else:
        return render(request,"secretary/login.html")

def myfamilyprofile(request):
    uid = User.objects.get(email = request.session['email'])
    mid = Members.objects.get(user_id=uid)
    all_members = Myfamily.objects.filter(user_id=uid)
    user_id = User.objects.get(role="Chairman")
    cid = Chairman.objects.get(user_id=user_id)
    return render(request,'secretary/dashboard/myfamilyprofile.html',{'uid':uid,'mid':mid,'all_members':all_members,'cid':cid})

def add_my_member(request):
    uid = User.objects.get(email = request.session['email'])    
    mid = Members.objects.get(user_id=uid)
    all_members = Myfamily.objects.filter(user_id=uid)

    if request.POST:
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        work = request.POST['work']
        contact = request.POST['contact']
        age = request.POST['age']
        gender = request.POST['gender']
        work = request.POST['work']
        blood_grp = request.POST['blood_grp']
        job_address = request.POST['job_address']
        birthdate = request.POST['birthdate']
        relation = request.POST['relation']
        profile_pic = request.POST['profile_pic']
        
        if request.FILES:
            mid.profile_pic = request.FILES['profile']
        Myfamily.objects.create(user_id=uid,firstname=firstname,lastname=lastname,contact=contact,age=age,gender=gender,work=work,blood_grp=blood_grp,job_address=job_address,birthdate=birthdate,relation=relation,profile_pic=profile_pic)
        return HttpResponseRedirect(reverse('myfamilyprofile'))
    else:
        return render(request,'secretary/dashboard/add_my_member.html',{'uid':uid,'mid':mid,'all_members':all_members})

def Editmyfamilyprofile(request):
    uid = User.objects.get(email = request.session['email'])    
    mid = Members.objects.get(user_id=uid)

    if request.POST:
        if request.FILES:
            mid.profile_pic = request.FILES['profile']
        return HttpResponseRedirect(reverse('myfamilyprofile'))
    else:
        return render(request,'secretary/dashboard/Editmyfamilyprofile.html',{'uid':uid,'mid':mid,'all_members':all_members})

def notice(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])    
        cid = Chairman.objects.get(user_id=uid)
        if request.POST:
            subject = request.POST['subject']
            description = request.POST['description']
            if "noticepic" in request.FILES:
                noticepic = request.FILES['noticepic']
                nid = NoticeBoard.objects.create(user_id = uid, subject=subject, description=description,profile_pic=noticepic)
            else:
                nid = NoticeBoard.objects.create(user_id = uid, subject=subject, description=description)
                print("---->",nall)
                nall = NoticeBoard.objects.order_by('-created_at')
                return render(request,"secretary/dashboard/notice-details.html",{'uid':uid,'cid':cid,'nall':nall})
            nall = NoticeBoard.objects.order_by('-created_at')
            return render(request,"secretary/dashboard/notice-details.html",{'uid':uid,'cid':cid,'nall':nall})
        else:
            return render(request,"secretary/dashboard/notice-page.html",{'uid':uid,'cid':cid})
    else:
        return HttpResponseRedirect(reverse('login'))

def notice_view(request):
    uid = User.objects.get(email = request.session['email'])    
    cid = Chairman.objects.get(user_id=uid)
    nall = NoticeBoard.objects.order_by('-created_at')
    return render(request,"secretary/dashboard/notice-details.html",{'uid':uid,'cid':cid,'nall':nall})

def memnotice_view(request):
    uid = User.objects.get(email = request.session['email'])    
    mid = Members.objects.get(user_id=uid)
    nall = NoticeBoard.objects.all()
    user_id = User.objects.get(role="Chairman")
    cid = Chairman.objects.get(user_id=user_id)

    return render(request,"secretary/dashboard/memnotice-details.html",{'uid':uid,'mid':mid,'nall':nall,'cid':cid})

def watchman_notice_view(request):
    uid = User.objects.get(email = request.session['email'])    
    wid = Watchman.objects.get(user_id=uid)
    nall = NoticeBoard.objects.all()
    user_id = User.objects.get(role="Chairman")
    cid = Chairman.objects.get(user_id=user_id)
    return render(request,"secretary/dashboard/watchman-notice-details.html",{'uid':uid,'wid':wid,'nall':nall,'cid':cid})

def delete_notice(request,pk):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        cid=Chairman.objects.get(user_id=uid)
        NoticeBoard.objects.filter(id=pk).delete()
        # nall=NoticeBoard.objects.get(id=pk)
        # nall.delete()
        nall = NoticeBoard.objects.order_by('-created_at')
        return render(request,"secretary/dashboard/notice-details.html",{'uid':uid,'cid':cid,'nall':nall})

def events(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])    
        cid = Chairman.objects.get(user_id=uid)
        if request.POST:
            subject = request.POST['subject']
            description = request.POST['description']

            if "eventpic" in request.FILES:
                eventpic = request.FILES['eventpic']
                eid = Events.objects.create(user_id = uid, subject=subject, description=description,profile_pic=eventpic)
            else:
                eid = Events.objects.create(user_id = uid, subject=subject, description=description)
                eall = Events.objects.order_by('-created_at')
                return render(request,"secretary/dashboard/event-details.html",{'uid':uid,'cid':cid,'eall':eall,'eid':eid})
            eall = Events.objects.order_by('-created_at')
            return render(request,"secretary/dashboard/event-details.html",{'uid':uid,'cid':cid,'eall':eall,'eid':eid})
        else:
            return render(request,"secretary/dashboard/event-page.html",{'uid':uid,'cid':cid})
    else:
        return HttpResponseRedirect(reverse('login'))

def event_view(request):
    uid = User.objects.get(email = request.session['email'])    
    cid = Chairman.objects.get(user_id=uid)
    eall = Events.objects.order_by('-created_at')
    return render(request,"secretary/dashboard/event-details.html",{'uid':uid,'cid':cid,'eall':eall})

def delete_event(request,pk):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        cid=Chairman.objects.get(user_id=uid)
        Events.objects.filter(id=pk).delete()
        # nall=NoticeBoard.objects.get(id=pk)
        # nall.delete()
        eall = Events.objects.order_by('-created_at')
        return render(request,"secretary/dashboard/event-details.html",{'uid':uid,'cid':cid,'eall':eall})

def add_complain(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])    
        mid = Members.objects.get(user_id=uid)
        if request.POST:
            subject = request.POST['subject']
            description = request.POST['description']

            clid = Complain.objects.create(user_id = uid, subject=subject, description=description)
            call = Complain.objects.order_by('-created_at')
            return render(request,"secretary/dashboard/complain_details.html",{'uid':uid,'mid':mid,'call':call,'clid':clid})
        else:
            return render(request,"secretary/dashboard/add_complain.html",{'uid':uid,'mid':mid})
    else:
        return HttpResponseRedirect(reverse('login'))

def complain_details(request):
    uid = User.objects.get(email = request.session['email'])    
    mid = Members.objects.get(user_id=uid)
    call = Complain.objects.order_by('-created_at')
    return render(request,"secretary/dashboard/complain_details.html",{'uid':uid,'mid':mid,'call':call})

def delete_complain(request,pk):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        mid=Members.objects.get(user_id=uid)
        Complain.objects.filter(id=pk).delete()
        # nall=NoticeBoard.objects.get(id=pk)
        # nall.delete()
        call = Complain.objects.order_by('-created_at')
        return render(request,"secretary/dashboard/complain_details.html",{'uid':uid,'mid':mid,'call':call})

def memeber_event_view(request):
    uid = User.objects.get(email = request.session['email'])    
    mid = Members.objects.get(user_id=uid)
    eall = Events.objects.order_by('-created_at')
    return render(request,"secretary/dashboard/member-event-details.html",{'uid':uid,'mid':mid,'eall':eall})

def chairman_complain_details(request):
    uid = User.objects.get(email = request.session['email'])    
    cid = Chairman.objects.get(user_id=uid)
    call = Complain.objects.order_by('-created_at')
    return render(request,"secretary/dashboard/chairman_complain_details.html",{'uid':uid,'cid':cid,'call':call})

def watchman_complain_details(request):
    uid = User.objects.get(email = request.session['email']) 
    user_id=User.objects.get(role="Chairman")
    print("-->",user_id)
    cid = Chairman.objects.get(user_id=user_id)   
    wid = Watchman.objects.get(user_id=uid)
    call = Complain.objects.order_by('-created_at')
    return render(request,"secretary/dashboard/watchman_complain_details.html",{'uid':uid,'wid':wid,'call':call,'cid':cid})

def watchman_add_complain(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email']) 
        user_id=User.objects.get(role="Chairman")
        print("-->",user_id)
        cid = Chairman.objects.get(user_id=user_id)   
        wid = Watchman.objects.get(user_id=uid)
        if request.POST:
            subject = request.POST['subject']
            description = request.POST['description']

            clid = Complain.objects.create(user_id = uid, subject=subject, description=description)
            call = Complain.objects.order_by('-created_at')
            return render(request,"secretary/dashboard/watchman_complain_details.html",{'uid':uid,'wid':wid,'call':call,'clid':clid,'cid':cid})
        else:
            return render(request,"secretary/dashboard/watchman_add_complain.html",{'uid':uid,'wid':wid,'cid':cid})
    else:
        return HttpResponseRedirect(reverse('login'))

def watchman_delete_complain(request,pk):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        wid=Watchman.objects.get(user_id=uid)
        Complain.objects.filter(id=pk).delete()
        # nall=NoticeBoard.objects.get(id=pk)
        # nall.delete()
        call = Complain.objects.order_by('-created_at')
        return render(request,"secretary/dashboard/watchman_complain_details.html",{'uid':uid,'wid':wid,'call':call})

def members_suggestion_box(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])    
        user_id=User.objects.get(role="Chairman")
        print("-->",user_id)
        cid = Chairman.objects.get(user_id=user_id)  
        mid = Members.objects.get(user_id=uid)
        if request.POST:
            subject = request.POST['subject']
            description = request.POST['description']

            sid = Suggestions.objects.create(user_id = uid, subject=subject, description=description)
            sall = Suggestions.objects.order_by('-created_at')
            return render(request,"secretary/dashboard/members_suggestion_box.html",{'uid':uid,'mid':mid,'sall':sall,'sid':sid,'cid':cid})
        else:
            return render(request,"secretary/dashboard/add_members_suggestions.html",{'uid':uid,'mid':mid,'cid':cid})
    else:
        return HttpResponseRedirect(reverse('login'))

def view_members_suggestion_box(request):
    uid = User.objects.get(email = request.session['email']) 
    user_id=User.objects.get(role="Chairman")
    print("-->",user_id)
    cid = Chairman.objects.get(user_id=user_id)     
    mid = Members.objects.get(user_id=uid)
    sall = Suggestions.objects.order_by('-created_at')
    return render(request,"secretary/dashboard/members_suggestion_box.html",{'uid':uid,'mid':mid,'sall':sall,'cid':cid})

def delete_members_suggestion(request,pk):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        mid=Members.objects.get(user_id=uid)
        Suggestions.objects.filter(id=pk).delete()
        # nall=NoticeBoard.objects.get(id=pk)
        # nall.delete()
        sall = Suggestions.objects.order_by('-created_at')
        return render(request,"secretary/dashboard/members_suggestion_box.html",{'uid':uid,'mid':mid,'sall':sall})

def watchman_suggestion_box(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])    
        user_id=User.objects.get(role="Chairman")
        print("-->",user_id)
        cid = Chairman.objects.get(user_id=user_id)  
        wid = Watchman.objects.get(user_id=uid)
        if request.POST:
            subject = request.POST['subject']
            description = request.POST['description']

            sid = Suggestions.objects.create(user_id = uid, subject=subject, description=description)
            sall = Suggestions.objects.order_by('-created_at')
            return render(request,"secretary/dashboard/watchman_suggestion_box.html",{'uid':uid,'wid':wid,'sall':sall,'sid':sid,'cid':cid})
        else:
            return render(request,"secretary/dashboard/add_watchman_suggestions.html",{'uid':uid,'wid':wid,'cid':cid})
    else:
        return HttpResponseRedirect(reverse('login'))

def view_watchman_suggestion_box(request):
    uid = User.objects.get(email = request.session['email']) 
    user_id=User.objects.get(role="Chairman")
    print("-->",user_id)
    cid = Chairman.objects.get(user_id=user_id)     
    wid = Watchman.objects.get(user_id=uid)
    sall = Suggestions.objects.order_by('-created_at')
    return render(request,"secretary/dashboard/watchman_suggestion_box.html",{'uid':uid,'wid':wid,'sall':sall,'cid':cid})


def delete_watchman_suggestion(request,pk):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        wid=Watchman.objects.get(user_id=uid)
        Suggestions.objects.filter(id=pk).delete()
        # nall=NoticeBoard.objects.get(id=pk)
        # nall.delete()
        sall = Suggestions.objects.order_by('-created_at')
        return render(request,"secretary/dashboard/watchman_suggestion_box.html",{'uid':uid,'wid':wid,'sall':sall})

def view_chairman_suggestion_box(request):
    uid = User.objects.get(email = request.session['email'])      
    cid = Chairman.objects.get(user_id=uid)
    sall = Suggestions.objects.order_by('-created_at')
    return render(request,"secretary/dashboard/chairman_suggestion_box.html",{'uid':uid,'sall':sall,'cid':cid})

def delete_chairman_suggestion(request,pk):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        cid=Chairman.objects.get(user_id=uid)
        Suggestions.objects.filter(id=pk).delete()
        # nall=NoticeBoard.objects.get(id=pk)
        # nall.delete()
        sall = Suggestions.objects.order_by('-created_at')
        return render(request,"secretary/dashboard/chairman_suggestion_box.html",{'uid':uid,'sall':sall,'cid':cid})

def add_vistiors(request):
    uid = User.objects.get(email = request.session['email'])    
    wid = Watchman.objects.get(user_id=uid)
    all_visitors = Vistiors.objects.filter(user_id=uid)
   
    if request.POST:
        member_firstname = request.POST['member_firstname']
        visitor_firstname = request.POST['visitor_firstname']
        house_no = request.POST['house_no']
        vechicle_deatails = request.POST['vechicle_deatails']
        contact = request.POST['contact']
        gender = request.POST['gender']
        currentdate = request.POST['currentdate']
        house= Members.objects.get(house_no=house_no)
    
        Vistiors.objects.create(user_id=uid,member_firstname=member_firstname,visitor_firstname=visitor_firstname,contact=contact,house_no=house,gender=gender,vechicle_deatails=vechicle_deatails,currentdate=currentdate)
        return render(request,'secretary/dashboard/add_my_visitor.html',{'uid':uid,'wid':wid,})
    else:
        return render(request,'secretary/dashboard/add_my_visitor.html',{'uid':uid,'wid':wid,'all_visitors':all_visitors})

def allvisitors(request):
    uid = User.objects.get(email = request.session['email'])
    user_id = User.objects.get(role="Chairman")
    cid = Chairman.objects.get(user_id=user_id) 
    wid = Watchman.objects.get(user_id=uid)
    vall = Vistiors.objects.all() # retrive all data from the model
      
    return render(request,'secretary/dashboard/Allvisitors.html',{'uid':uid,'wid':wid,'vall':vall,cid:'cid'})

def vistiordetails(request,d_pk):
    vid = Vistiors.objects.get(id = d_pk)  # for respective selected user
    uid = User.objects.get(email = request.session['email'])  # for logged in
    wid = Watchman.objects.get(user_id=uid)
    return render(request,'secretary/dashboard/visitor_details.html',{'uid':uid,'vid':vid,'wid':wid})

def image_gallery(request):
    uid = User.objects.get(email = request.session['email'])  # for logged in
    mid = Members.objects.get(user_id=uid)
   
    return render(request,'secretary/dashboard/image-gallery.html',{'uid':uid,'mid':mid})

def image_gallery_chairman(request):
    uid = User.objects.get(email = request.session['email'])  # for logged in
    cid = Chairman.objects.get(user_id=uid)
   
    return render(request,'secretary/dashboard/image-gallery-chairman.html',{'uid':uid,'cid':cid})

def image_gallery_watchman(request):
    uid = User.objects.get(email = request.session['email'])  # for logged in
    wid = Watchman.objects.get(user_id=uid)
   
    return render(request,'secretary/dashboard/image-gallery-watchman.html',{'uid':uid,'wid':wid})

def watchman_event_view(request):
    uid = User.objects.get(email = request.session['email'])    
    wid = Watchman.objects.get(user_id=uid)
    eall = Events.objects.order_by('-created_at')
    return render(request,"secretary/dashboard/watchman-event-details.html",{'uid':uid,'wid':wid,'eall':eall})

# def my_vistiordetails(request,pk):
#     vid = Vistiors.objects.get(id = pk) 
#     uid = User.objects.get(email = request.session['email'])
#     user_id = User.objects.get(role="Chairman")
#     cid = Chairman.objects.get(user_id=user_id) 
#     mid = Members.objects.get(user_id=uid)
#     vall = Vistiors.objects.get(user_id=uid) # retrive all data from the model
      
#     return render(request,"secretary/dashboard/myvisitors.html"{'uid':uid,'user_id':user_id,'cid':cid,'mid':mid,'vall':vall,'vid':vid})