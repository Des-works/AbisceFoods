from django.db import models
from PIL import Image

class Category(models.Model):
    name = models.CharField(max_length=20, blank=False)
    def __str__(self):
        return self.name
    
class Menu(models.Model):
    name = models.CharField(max_length=70, blank=False)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(default='', upload_to='food_pic', blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    def save(self, *args, **kwargs):



        super().save(*args, **kwargs)




        if self.image:



            try:



                img = Image.open(self.image.path)



                if img.height > 100 or img.width > 100:



                    output_size = (100, 100)



                    img.thumbnail(output_size)



                    img.save(self.image.path)



                elif img.height < 1 or img.width < 1:



                    output_size = (100, 100)



                    img.thumbnail(output_size)



                    img.save(self.image.path)



            except:
                pass

    def __str__(self):
        return self.name +' ' +'£ ' + self.price
    



class Event(models.Model):
    name = models.CharField(max_length=20, blank= False)
    breve_description = models.CharField(max_length = 90, blank= False)
    date_time = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(default='', upload_to='events_pic', blank=True)
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.image:
            try:
                img = Image.open(self.image.path)
                if img.height > 100 or img.width > 100:
                    output_size = (350, 450)
                    img.thumbnail(output_size)
                    img.save(self.image.path)
                elif img.height < 1 or img.width < 1:
                    output_size = (350, 450)
                    img.thumbnail(output_size)
                    img.save(self.image.path)
            except:
                pass
    


    def __str__(self):
        return self.name