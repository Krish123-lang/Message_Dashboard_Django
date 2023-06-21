from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from .models import Customer
from App.forms import Customerform, EmailForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from django.db.models import Q
from datetime import datetime
from django.core.mail import EmailMessage
from django.contrib.auth import logout
# Create your views here.


def home(request):
    return render(request, "home.html")


def send_message(request):
    if request.method == "POST":
        form = Customerform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Message sent successfully !!!")
        return HttpResponseRedirect('/')
    else:
        form = Customerform()
    return render(request, 'home.html', {'form': form})


@login_required(login_url="login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def inbox(request):

    if 'q' in request.GET:
        q = request.GET["q"]
        all_customer_list = Customer.objects.filter(
            Q(name__icontains=q) | Q(phone__icontains=q) | 
            Q(email__icontains=q) | Q(subject__icontains=q) | 
            Q(status__icontains=q) | Q(message__icontains=q)
        ).order_by('-created_at')
    else:
        all_customer_list = Customer.objects.all().order_by('-created_at')

    paginator = Paginator(all_customer_list, 10) # CHANGE THIS TO 10
    page = request.GET.get('page')
    all_customer = paginator.get_page(page)

    #============================ Messages Counter ============================
    # 1) TOTAL 
    total = Customer.objects.all().count()

    # 2) READ 
    read = Customer.objects.filter(status='Read').count()

    # 3) UNREAD 
    unread = Customer.objects.filter(status='Pending').count()

    # 4) TODAY 
    base = datetime.now().date()
    today = Customer.objects.filter(created_at__gt = base).count()

    context ={
        'customers': all_customer,
        'total': total,
        'read': read,
        'unread': unread,
        'today': today,
    }
    return render(request, "inbox.html", context)


@login_required(login_url="login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def delete_message(request, customer_id):
    customer = Customer.objects.get(id=customer_id)
    customer.delete()
    messages.success(request, "Message successfully deleted !")
    return HttpResponseRedirect('/inbox')


@login_required(login_url="login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def customer(request, customer_id):
    customer = Customer.objects.get(id=customer_id)
    if customer != None:
        return render(request, "customer.html", {"customer": customer})
    


@login_required(login_url="login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def mark_message(request):
    if request.method == "POST":
        customer = Customer.objects.get(id=request.POST.get('id'))
        if customer != None:
            customer.status = request.POST.get('status')
            customer.save()
            messages.success(request, "Message marked as read !!!")
            return HttpResponseRedirect('/inbox')
        

def AutoLogoutUser(request):
    logout(request)
    request.user = None
    messages.info(request, ".") # Because the argument can't be empty
    return HttpResponseRedirect('/')
    

#  ============================  ERRORS =============================

def E_500(request):
    return render(request, '500.html')


def E_404(request, exception):
    return render(request, '404.html')
