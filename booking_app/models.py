from django.db import models
from auth_system.models import User

class Room(models.Model):
    TYPE_CHOICES =  [
        ('standart', 'Standart'),
        ('lux', 'Lux'),
        ('suite', 'Suite'),
        ('family', 'Family'),
        ('single', 'Single'),
        ('double', 'Double'),
        ('twin', 'Twin'),
    ]
    
    title = models.CharField(max_length = 100)
    price = models.IntegerField()
    photo = models.ImageField(upload_to = 'rooms/', null = True, blank = True)
    description = models.TextField(null = True, blank = True)
    capacity  = models.IntegerField(default = 2)
    type_room = models.CharField(choices = TYPE_CHOICES, max_length = 50, default = 'standart')
    def __str__(self):
        return self.title
    
    
class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()
    persons = models.IntegerField(default = 1)
    phone_number = models.CharField(max_length = 15)
    created_at = models.DateTimeField(auto_now_add = True)
    def __str__(self):
        return f'Кімната: {self.room} - Дата заїзду: {self.check_in} Дата виїзду: {self.check_out}'