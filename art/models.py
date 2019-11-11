from django.db import models
from django.contrib.auth.models import User
# Create your models here.
def get_art_image_path(instance, filename):
    return 'art/%s/%s' % (instance.pk, filename)

# class Profile(models.Model):
#     objects =models.Manager()
#     nickname= models.TextField(max_length=10)
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     like_arts = models.ManyToManyField('Art',blank=True,related_name='likes_users')

#     def __str__(self):
#         return self.nickname
class Art(models.Model):
    objects =models.Manager()
    title = models .CharField(max_length =200)
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField(default='',max_length=500)
    image = models.ImageField(upload_to=get_art_image_path, default='')
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    like_count = models.PositiveIntegerField(default=0)
    likes = models.ManyToManyField(User, related_name='likes')
    price = models.TextField(default='',max_length =50)
    # category = models.CharField(max_length = 200)
    FASHION="fa"
    SCULPTURE="sc"
    CRAFT="cr"
    ETC="et"
    PAINTING="pa"
    CATEGORY_CHOICES = (
    (FASHION, "Fashion"),
    (SCULPTURE, "Sculpture"),
    (CRAFT,"Craft"),
    (ETC,"Etc"),
    (PAINTING,"Painting"),
    )
    category = models.CharField(
        max_length=2,
        choices=CATEGORY_CHOICES,
        default = ETC,
    )
    
    # @property
    # def total_likes(self):
    #     return self.likes.count()
    
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

class Like(models.Model) :
    objects = models.Manager()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    art = models.ForeignKey(Art, on_delete=models.CASCADE)