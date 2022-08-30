from .models import(Product)

def get_single_prod(productId):
    return Product.objects.get(pk=productId)