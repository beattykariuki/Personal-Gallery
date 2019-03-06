from django.test import TestCase
from .models import Category,Image,Location

# Create your tests here.
class Category_test(TestCase):
    def setUp(self):
        self.nature=Category(id=1,category_name="music")
    
    def test_instance(self):
        self.assertTrue(isinstance(self.nature,Category))

    def test_save_category(self):
        self.nature.save_category()
        category = Category.objects.all()
        self.assertTrue(len(category)>0)

    def test_delete_category(self):
        self.nature.delete_category()
        category= Category.objects.all()
        self.assertTrue(len(category) < 1)
