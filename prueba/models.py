from django.db import models
import datetime
#crear models es crear tablas en la base de datos
class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    
STATUS_CHOICES = [
    ('R', 'Reviewed'),
    ('N', 'Not Reviewed'),
    ('E', 'Error'),
    ('A', 'Accepted'),
    ('D', 'Denied'),
]
class Website(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='websites') 
    release_date = models.DateField(null=True, blank=True)
    rating = models.IntegerField()
    status = models.CharField(choices=STATUS_CHOICES, max_length=1,)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)  
    
    def was_released_last_week(self):
        if self.release_date < datetime.date(2020,6,6):
            return "Released before last week"
        else:
            return "Released last week or later"
        
    @property
    def get_full_name(self):
        return f"Este es el nombre completo del sitio web: {self.name}"
    