from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .forms import ReviewForm
from .models import Product

# Create your views here.

def home(request):
    products = Product.objects.all()
    return render(request, 'boutique/home.html',{"products":products})

def productDetail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'boutique/productdetail.html',{"product":product})


def productReview(request, pk):
    product = get_object_or_404(Product, pk=pk)
    reviews = product.reviews.all()  # Get all reviews for this product

    return render(request, 'boutique/productreviews.html', {
        'product': product,
        'reviews': reviews
    })
    
def addReview(request, pk):
    product = get_object_or_404(Product, pk=pk)
    reviews = product.reviews.all()  # Get all reviews for this product
    review_form = ReviewForm()

    if request.method == 'POST' and request.user.is_authenticated:
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            # Create and save the review
            review = review_form.save(commit=False)
            review.product = product
            review.user = request.user
            review.save()
            messages.success(request, "Thanks for your feedback!")
            return redirect('product-reviews', pk=pk)  # Redirect to the same page to see the new review

    return render(request, 'boutique/addreview.html', {
        'product': product,
        'reviews': reviews,
        'review_form': review_form
    })
    

def productCategory(request, category):
    products = Product.objects.filter(category = category)
    return render(request, 'boutique/category.html', {'products': products, 'category': category})
    