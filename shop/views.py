from math import ceil
from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact, Product, Order, OrderUpdate
import json

def index(request):
    allProds = []
    catProds = Product.objects.values('categrory', 'id')
    cats = {item['categrory'] for item in catProds}
    for cat in cats:
        prod = Product.objects.filter(categrory = cat)
        n = len(prod)
        nslides =  n//4 + ceil((n/4)-(n//4)) 
        allProds.append([prod, range(1, nslides), nslides])

    params = {"allProds" : allProds}
    return render(request, 'shop/index.html', params)


def searchMatch(query, item):
    if query in item.desc.lower() or query in item.product_name.lower() or query in item.categrory.lower():
        return True 
    else:
        return False

def search(request):
    query = request.GET.get('search')
    allProds = []
    catProds = Product.objects.values('categrory', 'id')
    cats = {item['categrory'] for item in catProds}
    for cat in cats:
        prodtemp = Product.objects.filter(categrory = cat)
        prod = [item for item in prodtemp if searchMatch(query, item)]

        n = len(prod)
        nslides =  n//4 + ceil((n/4)-(n//4)) 
        if len(prod) != 0:
            allProds.append([prod, range(1, nslides), nslides])

    params = {"allProds" : allProds, 'msg' : ""}
    if len(allProds) == 0 or len(query)<4:
        params = {'msg' : "Please make sure to enter relevent search query"}
    return render(request, 'shop/index.html', params)


def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    thank = False
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc =  request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
                         #Database name or doosra name contact k opr wala he 
        contact.save() 
        thank = True
    return render(request, 'shop/contact.html', {'thank' : thank})

# Tracking Code
def track(request):
    if request.method=="POST":
        order_id = request.POST.get('order_id', '')
        email = request.POST.get('email', '')

        # return HttpResponse(f"{order_id} and {email}")
 
        try:
            order = Order.objects.filter(order_id=order_id, email=email)
            if len(order)>0:
                update = OrderUpdate.objects.filter(order_id=order_id)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps({"status":"succes", "updates" : updates, "items_json" : order[0].items_json}, default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{"status" : "noitem"}')
        except Exception as e:
            return HttpResponse('{"status" : "error"}')

    return render(request, 'shop/track.html')





def productsView(request, myid):
    #Fetch product
    product = Product.objects.filter(id = myid)
    print(product)

    return render(request, 'shop/productsView.html', {'product' : product[0]})

def checkOut(request):
    if request.method=="POST":
        items_json = request.POST.get('items_json', '')
        name = request.POST.get('name', '')
        amount = request.POST.get('amount', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')
        order = Order(items_json=items_json, name=name, email=email, phone=phone, address=address, city=city, state=state, zip_code=zip_code, amount=amount)
                         #Database name or doosra name contact k opr wala he 
        order.save()
        
        update = OrderUpdate(order_id=order.order_id, update_desc="The order has been placed !")
        update.save()

        thank = True
        id = order.order_id
        return render(request, 'shop/checkOut.html', {'thank':thank, 'id':id})
    return render(request, 'shop/checkOut.html')