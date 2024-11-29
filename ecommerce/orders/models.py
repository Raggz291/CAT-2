from django.db import models

# Create your models here.
class Customer(models.Model):
    # Customer model to store customer information
    name = models.CharField(max_length=100)  # Customer's name
    email = models.EmailField(unique=True)    # Unique email for each customer

    def __str__(self):
        return self.name


class Order(models.Model):
    # Order model to store order information
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders')
    order_date = models.DateTimeField(auto_now_add=True)  # Automatically set the date when order is created
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)  # Total amount for the order

    def __str__(self):
        return f'Order {self.id} by {self.customer.name}'