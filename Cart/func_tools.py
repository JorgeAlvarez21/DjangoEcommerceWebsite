from Customers.models import CustomerInformation
from Cart.models import ShoppingCart
from Customers.func_tools import generateTransID
from Products.models import ProductInformation


class UserCart:
    def __init__(self, username):
        self.username = username
        self.user_query = CustomerInformation.objects.filter(username=self.username)
        if self.user_query:
            self.user_query = self.user_query[0]
            if self.user_query.transaction_id == None:
                self.transaction_id = generateTransID()
                CustomerInformation.objects.filter(username=self.username).update(transaction_id=self.transaction_id)
            else:
                self.transaction_id = self.user_query.transaction_id
        else:
            self.transaction_id = generateTransID()

    def addProduct(self, prod_id, prod_qty=1):
        products = ProductInformation.objects
        item = products.get(pk=prod_id)
        # Checking if the product has been added to this customer's cart
        prod = ShoppingCart.objects.filter(user_transaction_id=self.transaction_id, product_id=prod_id)

        if len(prod) == 0:
            prod_name = item.name
            prod_img = item.image
            prod_price = item.price
            prod_subtotal = round(float(prod_price * prod_qty), 2)
            prod_description = item.description
            prod_brand = item.brand
            new_entry = ShoppingCart(user_username=self.username, user_transaction_id=self.transaction_id,
                                     product_id=prod_id, product_name=prod_name, product_quantity=prod_qty,
                                     product_image=prod_img, product_price=prod_price, product_subtotal=prod_subtotal,
                                     product_description=prod_description, product_brand=prod_brand)
            new_entry.save()
        else:
            # Update quantity and subtotal of existent product
            self.UpdateQuantity(prod_id, prod_qty)

    def UpdateQuantity(self, prod_id, add_qty):
        try:
            prod = ShoppingCart.objects.filter(user_transaction_id=self.transaction_id, product_id=prod_id)
            product = prod[0]
            new_qty = product.product_quantity + add_qty

            if new_qty > 0:
                prod_subtotal = product.product_price * new_qty
                ShoppingCart.objects.filter(user_transaction_id=self.transaction_id, product_id=prod_id).update(
                    product_quantity=new_qty)
                ShoppingCart.objects.filter(user_transaction_id=self.transaction_id, product_id=prod_id).update(
                    product_subtotal=round(float(prod_subtotal), 2))
            if new_qty == 0:
                self.DeleteProduct(prod_id)
        except:
            pass

    def DeleteProduct(self, prod_id):
        try:
            product = ShoppingCart.objects.filter(user_transaction_id=self.transaction_id, product_id=prod_id)
            product.delete()
        except:
            product = ShoppingCart.objects.filter(user_transaction_id=self.transaction_id, product_id=prod_id)
            product[0].delete()
        return



def cartTotal(trans_id):
    total = 0
    cart_items = ShoppingCart.objects.all().filter(user_transaction_id=trans_id)
    for item in cart_items:
        total += item.product_subtotal

    return total
