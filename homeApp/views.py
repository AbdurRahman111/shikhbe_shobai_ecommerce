from django.shortcuts import render
from productApp.models import product_table, category_table, brand_table
# Create your views here.


def index(request):
    print("-------------Home page------------------")
    all_product = product_table.objects.all()
    print(all_product)
    context = {'all_product':all_product}
    return render(request, "index.html", context)



def product_details(request, product_slug):
    print("product_slug")
    print(product_slug)

    get_product_from_slug = product_table.objects.get(slug = product_slug)
    context = {
        'get_product_from_slug':get_product_from_slug,
    }
    return render(request, "product_details.html", context)


def help_func(request):
    return render(request, "help_func.html")


def support_func(request):
    return render(request, "support_func.html")

def contact_us_func(request):
    return render(request, 'contact_us_func.html')

def best_seller_func(request):
    return render(request, "best_seller_func.html")

def cart_page_func(request):
    return render(request, "cart_page_func.html")

def checkout_func(request):
    return render(request, "checkout_func.html")


def shop_func(request):

    get_category = request.GET.get('category')
    print(get_category)

    get_brand = request.GET.get('brand')
    print(get_brand)

   

    all_category_value = category_table.objects.all()
    all_brand_values = brand_table.objects.all()

    if get_category:
        get_category_row = category_table.objects.get(title = get_category)

        all_product_data = product_table.objects.filter(choose_category=get_category_row)
    elif get_brand:
        get_brand_row = brand_table.objects.get(title = get_brand)

        all_product_data = product_table.objects.filter(choose_brand=get_brand_row)
    else:
        all_product_data = product_table.objects.all()

    

    context = {
        'all_product_data':all_product_data,
        'all_category_value':all_category_value,
        'all_brand_values':all_brand_values,
        }
    return render(request, "shop_func.html", context)