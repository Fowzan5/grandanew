from django.shortcuts import render,HttpResponse,redirect
from rest_framework.views import APIView
from django.conf import settings
from django.core.mail import send_mail
from rest_framework.response import Response
from .models import UploadedImage
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def index_page(request):
    alll_pic = UploadedImage.objects.all()
    list_of_lists = [alll_pic[i:i+3] 
                    for i in range(0, len(alll_pic), 3)]

    return render(request,'index.html', {"pics":list_of_lists})

def rp_index(request):
    return render(request,'rp_index.html')

class EmailAPI(APIView):
    def get(self, request):
        subject = 'test'
        txt_ = 'hai'
        # html_ = self.request.GET.get('html')
        recipient_list = 'aswanthmvr@gmail.com'
        from_email = settings.DEFAULT_FROM_EMAIL

        sent_mail = send_mail(
            subject,
            txt_,
            from_email,
            recipient_list.split(','),
            # html_message=html_,
            fail_silently=False,
        )
        return HttpResponse({'msg': sent_mail}, status=200)
    

# @csrf_exempt
class Contact(APIView):
    def post(self, request):
        form_data = request.data.dict()
        name = form_data.get('name')
        email = form_data.get('email')
        phone = form_data.get('phoneNumber')
        msg = form_data.get('msg')
        city = form_data.get('city')
        message_email = settings.EMAIL_HOST_USER
        email_body = f"""
            Hello,

            You have a new site visit request from:

            Name : {name}
            e-mail : {email}
            Phone : {phone}
            City : {city}
            Query : {msg}

            Thank you!
            """
        send_mail(
            '<-noreplay->Mail from the Bloom Living site !',
            email_body,
            message_email,
            ['aswanthkannara@gmail.com',
             'zayed.fhd@gmail.com',
             'anwar@uaeaps.com'],
            fail_silently=False
        )
        # return redirect('/')
        return HttpResponse({'msg': 'true'}, status=200)
    def get(self,request):
        message_email = settings.EMAIL_HOST_USER
        form_data = request.query_params.dict()
        req_from = form_data.get('from')
        name = form_data.get('name')
        email = form_data.get('email')
        phone = form_data.get('phoneNumber')
        msg = form_data.get('msg')
        city = form_data.get('city')
        message_email = settings.EMAIL_HOST_USER
        email_body = f"""
            Hello,

            You have a new site visit request from:

            Name : {name}
            e-mail : {email}
            Phone : {phone}
            City : {city}
            Query : {msg}

            Source : {req_from}  website

            
            Thank you !
            """
        send_mail(
            '<-noreplay->Mail from the ' + req_from +' site !',
            email_body,
            message_email,
            ['aswanthkannara@gmail.com',
             'zayed.fhd@gmail.com',
             'anwar@uaeaps.com'
            ],
            fail_silently=False
        )
        return HttpResponse({'msg': 'sent_mail'}, status=200)