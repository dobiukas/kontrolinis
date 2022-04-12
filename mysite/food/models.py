from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.name)


class Category(models.Model):
    class Meta:
        verbose_name_plural = "categories"
    options = (
        ('breakfast', 'breakfast'),
        ('lunch', 'lunch'),
        ('dinner', 'dinner'),
        ('snacks', 'snacks'),
    )
    name = models.CharField(max_length=50, choices=options)

    def __str__(self):
        return self.name


class Food(models.Model):
    name = models.CharField(max_length=200)
    category = models.ManyToManyField(Category)
    carbohydrate = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    fats = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    protein = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    calorie = models.DecimalField(max_digits=5, decimal_places=2, default=0, blank=True)
    quantity = models.IntegerField(default=1, null=True, blank=True)

    def __str__(self):
        return str(self.name)


# for user page-------------------------------------------------------------
class UserFood(models.Model):
    customer = models.ManyToManyField(Customer, blank=True)
    food = models.ManyToManyField(Food)
# status

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    date = models.DateField('Date', null=True, blank=True)

    ORDER_STATUS = (
        ('e', 'Entered'),
        ('w', 'Waiting'),
        ('p', 'In progress'),
        ('c', 'Completed'),
        )

    status = models.CharField(
        max_length=1,
        choices=ORDER_STATUS,
        blank=True,
        default='e',
        help_text='Status',
        )

    def __str__(self):
        return f"{self.user.first_name} order No.{self.id} on {self.date}."