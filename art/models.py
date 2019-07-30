from django.db import models
from django.contrib.auth.models import User
# Create your models here.
def get_art_image_path(instance, filename):
    return 'art/%s/%s' % (instance.pk, filename)
    
class Art(models.Model):
    objects =models.Manager()
    title = models .CharField(max_length =200)
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField(default='',max_length=500)
    image = models.ImageField(upload_to=get_art_image_path, default='')
    user=models.ForeignKey(User, on_delete=models.CASCADE)


    def save(self, *args, **kwargs):
        if self.pk is None:
            temp_image = self.image
            self.image = None
            super().save(*args, **kwargs)
            self.image = temp_image
        super().save(*args, **kwargs)
    def __str__ (self) :
        return self.title

class ArtComent(models.Model):
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    art = models.ForeignKey(Art, on_delete=models.CASCADE)