from django.db import models
from django.contrib.auth import get_user_model

User=get_user_model()

class Orders(models.Model):
    PIZZA_SIZES=(
        ('SMALL','Small'),
        ('MEDIUM','Medium'),
        ('LARGE','Large'),
        ('EXTRA_LARGE','Extra_Large'),
    )

    ORDER_STATUSES=(
        ('PENDING','Pending'),
        ('IN_TRANSIT','In_Transit'),
        ('DELIVERED','delivered')
    )

    order_status=models.CharField(max_length=25,choices=ORDER_STATUSES,default=ORDER_STATUSES[0][0])
    size=models.CharField(max_length=25,choices=PIZZA_SIZES,default=PIZZA_SIZES[0][0])
    quantity=models.IntegerField()
    flavour=models.CharField(max_length=40)
    customer=models.ForeignKey(User,on_delete=models.CASCADE)
    placed_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
