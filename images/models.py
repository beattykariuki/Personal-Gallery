from django.db import models

# Create your models here.
class Location(models.Model):
    location_name = models.CharField(max_length =40)

    def __str__(self):
        return self.location_name

class Category(models.Model):
    category_name = models.CharField(max_length =40)

    def save_category(self):
        self.save()

    def delete_category(self):
        # category= Category.objects.get(category_name='nature')
        self.delete()

    def __str__(self):
        return self.category_name

class Image(models.Model):
    title = models.CharField(max_length =40)
    description = models.CharField(max_length =40)
    location = models.ForeignKey(Location)
    category = models.ForeignKey(Category)
    image_path = models.ImageField(upload_to = 'images/')

    def __str__(self):
        return self.title

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def search_by_category(cls,search_term):
        result_search = cls.objects.filter(category__category_name__icontains=search_term)
        return result_search

    @classmethod
    def filter_by_location(cls,location):
        filter_by_location = cls.objects.filter_by(location__location_name__icontains=location)
        return filter_by_location

    @classmethod
    def get_image_by_id(cls,input_id):
        get_image_by_id = cls.objects.get(id=input_id)
        return get_image_by_id

    @classmethod
    def retrieve_all(cls):
        all_images = Image.objects.all()
        return all_images
    

