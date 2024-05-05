# checkout_management.py

from models import Checkout
# """Represents a checkout record in the library.
    
#     Attributes:
#         user_id (str): The ID of the user who checked out the item.
#         isbn (str): The ISBN of the item that was checked out.
#     """
class CheckoutManager:
    def __init__(self):
        self.checkouts = []

    def checkout_book(self, user_id, isbn):
        self.checkouts.append(Checkout(user_id, isbn))
