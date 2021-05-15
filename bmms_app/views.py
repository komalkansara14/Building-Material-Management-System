from django.shortcuts import render
from .models import *
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.conf import settings
from django.core.mail import send_mail
import random
from .paytm import generate_checksum, verify_checksum
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
global cprice,bprice,sprice
def index(request):
    
    user = UserRegistration.objects.get(email=request.session['email'])
    go = GoDownStock.objects.all()
    cement = 0
    sand = 0
    bricks = 0
    global cprice,bprice,sprice
    for i in go:
        
        cement += i.cement_amount
        sand += i.sand_amount
        bricks += i.brick_amount
        cprice = i.cement_price + 50
        sprice = i.sand_price + 50
        bprice = i.brick_price + 10
    
    return render(request,'index.html',
    {'user':user,'cement':cement,'bricks':bricks,'sand':sand,'cprice':cprice, 'sprice':sprice, 'bprice':bprice})

def home(request):
    return render(request, 'home.html')

def transporter_index(request):
    transporter = TransporterRegistration.objects.get(email = request.session['email'])
    return render(request, 'transporter_index.html', {'transporter':transporter})

def elements(request):
    return render(request, 'elements.html')

def generic(request):

    if request.method == "POST":
        cs = ContactUs.objects.create(
            name = request.POST['name'],
            email = request.POST['email'],
            subject = request.POST['subject'],
            message = request.POST['message'],
        )

        cs.save()
        return HttpResponse('<h1 style="text-align:center; color:green;">Your message has been sent successfully!!!</h1>')
    else:
        return render(request, 'generic.html')

def user_register(request):
    if request.method == "POST":
        try:
            ur = UserRegistration.objects.get(email=request.POST['email']) # email: model (User Registration) field and ['email']: name attribute in form (user_registration.html)
            msg = 'Email already exist'
            return render(request, 'user_registration.html',{'msg':msg})

        except:
            
            if ((request.POST['email']) == (request.POST['cemail'])):
                ur = UserRegistration.objects.create(
                    name = request.POST['name'],
                    email = request.POST['email'],
                    cemail = request.POST['cemail'],
                    password = request.POST['password'],
                    #cpassword = request.POST['cpassword'],
                    phone_no = request.POST['phone_no'],
                    address = request.POST['address'],
                )
                ur.save()
                email = request.POST['email']
                otp = random.randint(1000,9999)
                subject = 'OTP for Sign up'
                message = f'Hello Your OTP for successfully sign up is {otp}'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [email, ]
                print('----------------------------------------')
                send_mail( subject, message, email_from, recipient_list )

                return render(request,'otp.html',{'otp':otp,'email':email})
            

    else:
        msg = 'Registration failed!!!'
        return render(request, 'user_registration.html', {'msg':msg})

def transporter_register(request):

    if request.method == 'POST':

        try:

            tr = TransporterRegistration.objects.get(email = request.POST['email'])
            msg = 'Email already exist' 
            return render(request, 'transporter_registration.html', {'msg':msg})
        
        except:

            if((request.POST['email']) == (request.POST['cemail'])):

                tr = TransporterRegistration.objects.create(
                    name = request.POST['name'],
                    email = request.POST['email'],
                    cemail = request.POST['cemail'],
                    password = request.POST['password'],
                    #cpassword = request.POST['cpassword'],
                    phone_no = request.POST['phone_no'],
                    vehicle_no = request.POST['vehicle_no'],
                    address = request.POST['address'],

                )
                tr.save()
                email = request.POST['email']
                otp = random.randint(1000, 9999)

                subject = 'OTP for Sign up'
                message = f'Hello Your OTP for successfully sign up is {otp}'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [email, ]
                print('----------------------------------------')
                send_mail( subject, message, email_from, recipient_list )
                
                return render(request,'otp_transporter.html',{'otp':otp,'email':email})

    else:
        msg = 'Registration failed!!!'
        return render(request, 'transporter_registration.html', {'msg':msg})


    #return render(request, 'transporter_registration.html')

def otp_verify(request):
    if request.method == "POST":
        if request.POST['eotp'] == request.POST['otp']:
            user = UserRegistration.objects.get(email=request.POST['email'])
            user.verify = True
            user.save()
            return render(request,'login.html')
        else:
            msg = 'OTP is not matched'
            otp = request.POST['otp']
            return render(request,'otp.html',{'otp':otp,'msg':msg})
    else:
        return render(request, 'otp.html')

def otp_verify_transporter(request):
    
    if request.method == "POST":
        if request.POST['eotp'] == request.POST['otp']:

            transporter = TransporterRegistration.objects.get(email = request.POST['email'])
            transporter.verify = True
            transporter.save()
            
            return render(request, 'transporter_login.html')
        
        else:
            msg = 'OTP is not matched'
            otp = request.POST['otp']
            
            return render(request, 'otp_transporter.html', {'otp':otp, 'msg':msg})

    else:
        return render(request, 'otp_transporter.html')

    

def login(request):
    if request.method == "POST":
        try:
            user = UserRegistration.objects.get(email=request.POST['email'])
            if user.password == request.POST['password']:
                request.session['email'] = request.POST['email']
                # print(request.session['email'])
                go = GoDownStock.objects.all()
                cement = 0
                sand = 0
                bricks = 0
                global cprice,bprice,sprice
                for i in go:
                    cement += i.cement_amount
                    sand += i.sand_amount
                    bricks += i.brick_amount
                    cprice = i.cement_price + 50
                    sprice = i.sand_price + 50
                    bprice = i.brick_price + 10

                return render(request,'index.html',
                {'user':user,'cement':cement,'bricks':bricks,'sand':sand,'cprice':cprice, 'sprice':sprice, 'bprice':bprice})

            else:
                msg = 'Incorrect Username or Password'
                return render(request,'login.html',{'msg':msg})

        except:
            msg = 'Invalid Email'
            return render(request,'login.html',{'msg':msg})
    else:
        return render(request, 'login.html')

def transporter_login(request):

    if request.method == "POST":

        try:
            transporter = TransporterRegistration.objects.get(email = request.POST['email'])

            if transporter.password == request.POST['password']:

                request.session['email'] = request.POST['email']

                '''go = GoDownStock.objects.all()
                cement = 0
                sand = 0
                bricks = 0
                for i in go:
                    cement += i.cement_amount
                    sand += i.sand_amount
                    bricks += i.brick_amount
                    cprice = i.cement_price + 50
                    sprice = i.sand_price + 50
                    bprice = i.brick_price + 10'''

                return render(request,'transporter_index.html')
                
            
            else:
                msg = 'Incorrect Username or password'
                return render(request, 'transporter_login.html', {'msg':msg})
        
        except:

            msg = 'Invalid Email'
            return render(request, 'transporter_login.html', {'msg':msg})
    
    else:

        return render(request, 'transporter_login.html')
    
    #return render(request, 'transporter_login.html')

def logout(request):
    del request.session['email']
    go = GoDownStock.objects.all()
    cement = 0
    sand = 0
    bricks = 0
    for i in go:
        cement += i.cement_amount
        sand += i.sand_amount
        bricks += i.brick_amount
        cprice = i.cement_price + 50
        sprice = i.sand_price + 50
        bprice = i.brick_price + 10
    
    return render(request,'index.html',
        {'cement':cement,'bricks':bricks,'sand':sand,'cprice':cprice, 'sprice':sprice, 'bprice':bprice})
    #return render(request,'index.html')

def transporter_logout(request):
    del request.session['email']
    return render(request, 'transporter_index.html')

def godownstock(request):

    if request.method == "POST":

        gds = GoDownStock.objects.create(

            material_name = request.POST['material_name'],
            quantity = request.POST['quantity'],
            unit_price = request.POST['unit_price'],
        
        )
        gds.save()
        total = quantity * unit_price
        return HttpResponse('<h1 style="color:green;">Material is added succesfully...</h1>')

    else:
        
        return render(request, 'godownstock.html')

def seller(request):
    pass 

def admin_login(request):

    return render(request, 'admin_login.html')

def user_forgot(request):
    if request.method == "POST":
        try:
            
            user = UserRegistration.objects.get(email=request.POST['email'])
            email = request.POST['email']
            otp = random.randint(1000,9999)
            subject = 'OTP for password change'
            msg = f'Hello, Your OTP for Reset password {otp}'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email, ]
            print('---------------------------------------------')
            send_mail( subject, msg, email_from, recipient_list )
            return render(request,'user_forgot_otp.html',{'otp':otp,'email':email})


        except:
            msg = 'First Sign up and then login'
            return render(request,'user_registration.html',{'msg':msg}) 

    else:
        return render(request,'user_forgot.html')

def forgot_otp(request):
    if request.method == "POST":
        otp = request.POST['otp']
        eotp = request.POST['eotp']
        email = request.POST['email']
        if otp == eotp:
            return render(request,'user_reset_password.html',{'email':email})
        else:
            msg = 'OTP does not matched'
            return render(request,'user_forgot_otp.html',{'msg':msg,'otp':otp,'email':email})
    
    else:
        return render(request,'user_forgot_otp.html')

def user_reset_password(request):
    if request.method == "POST":
        if request.POST['password'] == request.POST['cpassword']:
            print(request.POST['email'])
            user = UserRegistration.objects.get(email=request.POST['email'])
            user.password = request.POST['password']
            #user.cpassword = request.POST['cpassword']
            user.save()
            return render(request,'login.html')


        else:
            msg = 'Password does not matched'
            return render(request,'user_reset_password.html',{'msg':msg})

    else:
        return render(request,'user_reset_password.html')

def change_password(request):

    if request.method == "POST":
        
        if request.POST['npassword'] == request.POST['cnpassword']:

            user = UserRegistration.objects.get(email = request.session['email'])

            if user.password == request.POST['opassword']:
                
                
                npassword = request.POST['npassword']
                cnpassword = request.POST['cnpassword']
                user.password = request.POST['npassword']
            
            user.save()
            go = GoDownStock.objects.all()
            cement = 0
            sand = 0
            bricks = 0
            for i in go:
                cement += i.cement_amount
                sand += i.sand_amount
                bricks += i.brick_amount
                cprice = i.cement_price + 50
                sprice = i.sand_price + 50
                bprice = i.brick_price + 10
            
            return render(request,'index.html',
            {'cement':cement,'bricks':bricks,'sand':sand,'cprice':cprice, 'sprice':sprice, 'bprice':bprice})
            
            #return render(request, 'index.html')
        
        else:
            msg = 'Password is not matched'
            return render(request, 'change_password.html', {'msg':msg})

    else:
        return render(request, 'change_password.html')

def transporter_forgot(request):

    if request.method == "POST":

        try:

            transporter = TransporterRegistration.objects.get(email = request.POST['email'])
            email = request.POST['email']
            otp = random.randint(1000, 9999)
            subject = 'OTP to reset the password'
            message = f'Hello, your OTP for reset password {otp}'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email, ]
            print('---------------------------------------------')
            send_mail( subject, message, email_from, recipient_list )
            return render(request, 'transporter_forgot_otp.html',{'otp':otp, 'email':email})

        except:

            msg = 'First Sign up and then login'
            return render(request, 'transporter_registration.html', {'msg':msg})
    
    else:
        return render(request, 'transporter_forgot.html')

def transporter_forgot_otp(request):

    if request.method == "POST":

        otp = request.POST['otp']
        eotp = request.POST['eotp']
        email = request.POST['email']

        if otp == eotp:
            return render(request, 'transporter_reset_password.html', {'email':email})
        
        else:
            msg = 'OTP is not matched'
            return render(request, 'transporter_forgot_otp.html', {'msg':msg, 'otp':otp, 'email':email})
    
    else:
        return render(request, 'transporter_forgot_otp.html')

def transporter_reset_password(request):

    if request.method == "POST":

        if request.POST['password'] == request.POST['cpassword']:

            transporter = TransporterRegistration.objects.get(email = request.POST['email'])
            transporter.password = request.POST['password']
            transporter.save()
            return render(request, 'transporter_login.html')
        
        else:
            msg = 'Password does not match'
            return render(request, 'transporter_reset_password.html')

    else:
        return render(request, 'transporter_reset_password.html')

def transporter_change_password(request):

    if request.method == "POST":

        if request.POST['npassword'] == request.POST['cnpassword']:

            transporter = TransporterRegistration.objects.get(email = request.session['email'])

            if transporter.password == request.POST['opassword']:
                npassword = request.POST['npassword']
                cnpassword = request.POST['cnpassword']
                transporter.password = request.POST['cnpassword']
            
            transporter.save()

            return render(request, 'transporter_index.html')
        else:
            msg = 'Password is not matched!!'
            return render(request, 'transporter_change_password.html', {'msg':msg})
    
    else:
        return render(request, 'transporter_change_password.html')
    #return render(request, 'transporter_change_password.html')

def buy_now_sand(request):
    if request.method == 'POST':
        
        user = UserRegistration.objects.get(email=request.session['email'])
        total = int(request.POST['quantity']) * int(sprice)
        address = request.POST['address']
        quantity = request.POST['quantity']
        order = Order.objects.create(
            user=user,
            material_name='Sand',
            quantity = request.POST['quantity'],
            price=request.POST['sprice'],
            address=request.POST['address'],
            total_amount = total,
        )
        order.save()
        return render(request,'order_sand_details.html',{'total':total,'user':user,'address':address,'quantity':quantity})


    else:
        return render(request, 'buy_now_sand.html',{'sprice':sprice})

def buy_now_cement(request):

    if request.method == 'POST':
        
        user = UserRegistration.objects.get(email=request.session['email'])
        total = int(request.POST['quantity']) * int(cprice)
        address = request.POST['address']
        quantity = request.POST['quantity']
        order = Order.objects.create(
            user=user,
            material_name='Cement',
            quantity = request.POST['quantity'],
            price=request.POST['cprice'],
            address=request.POST['address'],
            total_amount = total,
        )
        order.save()
        return render(request,'order_cement_details.html',{'total':total,'user':user,'address':address,'quantity':quantity})

    else:
        return render(request, 'buy_now_cement.html', {'cprice':cprice})

def buy_now_bricks(request):
    if request.method == 'POST':
        
        user = UserRegistration.objects.get(email=request.session['email'])
        total = int(request.POST['quantity']) * int(bprice)
        address = request.POST['address']
        quantity = request.POST['quantity']
        order = Order.objects.create(
            user=user,
            material_name='Bricks',
            quantity = request.POST['quantity'],
            price=request.POST['bprice'],
            address=request.POST['address'],
            total_amount = total,
        )
        order.save()
        return render(request,'order_bricks_details.html',{'total':total,'user':user,'address':address,'quantity':quantity})


    else:
        return render(request, 'buy_now_bricks.html', {'bprice':bprice})

def initiate_payment(request,pk):

    global temp
    temp = pk
    if request.method == "GET":
        order = Order.objects.get(pk=pk)
        total = order.total_amount
        return render(request, 'pay.html',{'total':total,'pk':pk})

    try:
        
        amount = int(request.POST['amount'])
        user = UserRegistration.objects.get(email = request.session['email'])
    
    except:
        return render(request, 'pay.html', context={'error': 'Wrong Accound Details or amount'})
    
    transaction = Transaction.objects.create(made_by=user, amount=amount)
    transaction.save()
    merchant_key = settings.PAYTM_SECRET_KEY

    params = (
        ('MID', settings.PAYTM_MERCHANT_ID),
        ('ORDER_ID', str(transaction.order_id)),
        ('CUST_ID', str(request.session['email'])),
        ('TXN_AMOUNT', str(transaction.amount)),
        ('CHANNEL_ID', settings.PAYTM_CHANNEL_ID),
        ('WEBSITE', settings.PAYTM_WEBSITE),
        # ('EMAIL', request.user.email),
        # ('MOBILE_N0', '9911223388'),
        ('INDUSTRY_TYPE_ID', settings.PAYTM_INDUSTRY_TYPE_ID),
        ('CALLBACK_URL', 'http://127.0.0.1:8000/callback/'),
        # ('PAYMENT_MODE_ONLY', 'NO'),
    )

    paytm_params = dict(params)
    checksum = generate_checksum(paytm_params, merchant_key)

    transaction.checksum = checksum
    transaction.save()

    paytm_params['CHECKSUMHASH'] = checksum
    print('SENT: ', checksum)
    return render(request, 'redirect.html', context=paytm_params)

@csrf_exempt
def callback(request):

    if request.method == 'POST':
        received_data = dict(request.POST)
        paytm_params = {}
        paytm_checksum = received_data['CHECKSUMHASH'][0]

        for key, value in received_data.items():
            if key == 'CHECKSUMHASH':
                paytm_checksum = value[0]
            else:
                paytm_params[key] = str(value[0])
        
        # Verify checksum
        is_valid_checksum = verify_checksum(paytm_params, settings.PAYTM_SECRET_KEY, str(paytm_checksum))
        if is_valid_checksum:
            l = ['0','1','2','3','4','5','6','7','8','9','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',]
            global temp
            order = Order.objects.get(pk = temp)
            order.status = 'Active'
            order.save()
            po = PaidOrder.objects.create(
                order = order,
                pay_id = ''.join(random.choices(l, k = 8))
            )
            del temp
            received_data['message'] = "Checksum Matched"
        else:
            received_data['message'] = "Checksum Mismatched"
            return render(request, 'callback.html', context=received_data)
        #user = request.session['email']
        return render(request, 'callback.html', context=received_data)

def order_bricks_details(request):
    total = request.POST['total']
    return render(request, 'index.html',{'total':total})

def order_sand_details(request):
    total = request.POST['total']
    return render(request, 'index.html',{'total':total})

def order_cement_details(request):
    total = request.POST['total']
    return render(request, 'index.html',{'total':total})

def cart(request):
    #user = UserRegistration.objects.get(email=request.session['email'])
    order = Order.objects.all()
    return render(request,'cart.html', {'order':order})

def delete_item(request,pk):
    order = Order.objects.get(pk=pk)
    order.delete()
    return HttpResponseRedirect(reverse('cart'))

def update_order(request,pk):
    order = Order.objects.get(pk=pk)
    if request.method == 'POST':
        order.quantity = request.POST['quantity']
        order.address = request.POST['address']
        order.total_amount = int(order.price) * int(request.POST['quantity'])
        order.save()
        return HttpResponseRedirect(reverse('cart'))

    else:
        return render(request, 'update_order.html',{'pk':pk,'order':order})

def my_order(request):
    order = PaidOrder.objects.all()
    return render(request, 'my_order.html',{'order':order})

def delivery_details(request):
    
    order = PaidOrder.objects.all()
    return render(request, 'delivery_details.html', {'order':order})

def remaining_delivery(request):
    order = PaidOrder.objects.all()
    return render(request, 'remaining_delivery.html',{'order':order})

def update_delivery(request,pk):

    order = PaidOrder.objects.get(pk=pk)
    if request.method == 'POST':
        order.remarks = request.POST['remarks']
        order.save()
        return HttpResponseRedirect(reverse('remaining_delivery'))
    
    else:
        return render(request, 'update_delivery.html', {'pk':pk, 'order':order})

def completed_delivery(request):

    cd = CompletedDelivery.objects.all()
    return render(request, 'completed_delivery.html', {'cd':cd})



def complete_order(request,pk):
    order = PaidOrder.objects.get(pk=pk)
    CompletedDelivery.objects.create(
        delivered = order,
        status="Completed"
    )

    s = order.order
    s.status = 'Completed'
    s.save()
    
    return HttpResponseRedirect(reverse('remaining_delivery'))

