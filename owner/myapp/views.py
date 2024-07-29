from django.shortcuts import render,redirect,get_object_or_404
from .models import *

# Create your views here.
# views.py
from django.shortcuts import render

def customer_page(request):
    customers=Customer.objects.all()

    query = request.GET.get('q', '')  # Get the 'q' parameter from the query string (default to empty string)
    
    if query:
        customers = Customer.objects.filter(name__icontains=query)  # Filter customers by name containing the query
    else:
        customers = Customer.objects.all()  # Get all customers if no search query is provided
    
    context = {
        "customers": customers,
        "query": query,  # Pass the query back to the template for display purposes
    }
    context={
        "customers":customers
    }
    return render(request, 'customer_page.html',context)

def products_page(request):
    products=Product.objects.all()
    context={
        "products":products
    }

    return render(request, 'products_page.html',context)

def Category_page(request):
    categaries=Category.objects.all()
    context={
        "categaries":categaries
    }

    return render(request, 'Category_page.html',context)

def Transactions(request):
    transactions=Transaction.objects.all()
    context={
        "transactions":transactions
    }
    return render(request, 'Transactions.html',context)

from django.shortcuts import render, redirect
from .forms import CategoryForm, ProductForm, CustomerForm

def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Category_page')  # Replace 'success_url' with your desired redirect URL
    else:
        form = CategoryForm()
    return render(request, 'category_create.html', {'form': form})

def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products_page')  # Replace 'success_url' with your desired redirect URL
    else:
        form = ProductForm()
    return render(request, 'product_create.html', {'form': form})

def customer_create(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_page')  # Replace 'success_url' with your desired redirect URL
    else:
        form = CustomerForm()
    return render(request, 'customer_create.html', {'form': form})

def customer_details(request,id):
    print(id)
    customer=Customer.objects.get(id=id)
    context={
        "customer":customer

    }
    return render(request,'customer_details.html',context)

def product_details(request,id):
    products=Product.objects.get(id=id)
    context={
        "products":products

    }
    return render(request,'product_details.html',context)

def customer_update(request,id):
    customer=Customer.objects.get(id=id)
    context={
        "customer":customer

    }

    return render(request,'customer_update.html',context)

def product_update(request,id):
    product=Product.objects.get(id=id)
    context={
        "product":product
    }

    return render(request,'product_update.html',context)

def successfully_updated_product(request,id):
    product=Product.objects.get(id=id)
    if request.method == 'POST':
        # Get values from request.POST with default values as empty strings
        name=request.POST.get('name', '')
        price=request.POST.get('price', '')
        quantity=request.POST.get('quantity', '')
        selling_no=request.POST.get('selling_no', '')
        model_or_brand=request.POST.get('model', '')
        product.name=name
        product.price=price
        product.quantity=quantity
        product.selling_no=selling_no
        product.model_or_brand=model_or_brand
        product.save()
    return redirect("product_details",id=id)

def customer_delete(request,id):
    customer=Customer.objects.get(id=id)
    customer.delete()

    return redirect('customer_page')

def product_delete(request,id):
    product=Product.objects.get(id=id)
    product.delete()
    return redirect('products_page')

def category_delete(request,id):
    category=Category.objects.get(id=id)
    category.delete()
    return redirect('Category_page')


def successfully_updated(request,id):
    customer=Customer.objects.get(id=id)
    print(customer)
    if request.method == 'POST':
        # Get values from request.POST with default values as empty strings
        username = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone_number=request.POST.get('phone_number','')
        gender=request.POST.get('gender','')
        pannumber=request.POST.get('pan_number','')

        print(username,email)
        customer.name=username
        customer.email=email
        customer.pan_number=phone_number
        customer.gender=gender
        customer.pan_number=pannumber
        customer.save()
    return redirect("customer_details",id=id)

def Add_product_to_the_customer(request,id):
    customer = get_object_or_404(Customer, id=id)
    products=Product.objects.all()

    context={
        "customer":customer,
        "products":products

    }

    return render(request,"Add_product_to_the_customer.html",context)


def successfully_added_to_customer(request,product_id,customer_id):
    productn=Product.objects.get(id=product_id)
    product_number=productn.quantity
    no_of_products=productn.selling_no

    print(product_number,no_of_products)
    productn.quantity=product_number-1
    productn.selling_no=no_of_products+1
    productn.save()
    print(productn.selling_no,productn.quantity)
    customer = Customer.objects.get(id=customer_id)
    transaction=Transaction.objects.create(customer=customer,product=productn)

    all=Transaction.objects.all()
    print(all)

    product = Product.objects.get(id=product_id)
    customer.products.add(product)
    customer.save()
    return redirect('customer_details',customer_id)