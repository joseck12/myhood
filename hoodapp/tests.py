from django.test import TestCase
from .models import hoodpro,Profile,Post,Business
# Create your tests here.

# Create your tests here.
#profile test
class ProfileTestClass(TestCase):
     #set Up method
    def setUp(self):
        self.joseck = Profile(id=9000,username = 'joseck')
    #testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.joseck,Profile))
    #testing save method
    def test_save_method(self):
        self.joseck.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)
    #testing for deleting method
    def test_delete_method(self):
        self.joseck.save_profile()
        self.joseck.delete_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile) > 0)
    #testing for update caption
    def test_update_metod(self):
        self.joseck.save_profile()
        self.joseck.update_description()
        profile = Profile.objects.all()
        self.assertTrue(len(profile) > 0)
    #testing for creatinging post
    def test_creation_method(self):
        self.joseck.create_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile) > 0)
class PostTestClass(TestCase):
    #set Up method
    def setUp(self):
        self.image = Post(image = 'cool')
    #test instance
    def test_instance(self):
        self.assertTrue(isinstance(self.image,Post))
    def test_save_method(self):
        self.image.save_image()
        image = Post.objects.all()
        self.assertTrue(len(image) > 0)
    #testing for deleting method
    def test_delete_method(self):
        self.image.save_image()
        self.image.delete_image()
        image = Post.objects.all()
        self.assertTrue(len(image) > 0)
    #testing for update caption
    def test_update_metod(self):
        self.image.save_image()
        self.image.update_caption()
        image = Post.objects.all()
        self.assertTrue(len(image) > 0)
    #testing for creatinging post
    def test_creation_method(self):
        self.image.create_post()
        post = Post.objects.all()
        self.assertTrue(len(post) > 0)
class BusinessTestClass(TestCase):
    #set up method
    def setUp(self):
        self.business = Business(id=9000,business_name= 'joseck')
    #testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.business,Business))
    #testing for saving
    def test_save_method(self):
        self.business.save_business()
        business = Business.objects.all()
        self.assertTrue(len(business) > 0)
    #testing for deleting method
    def test_delete_method(self):
        self.business.save_business()
        self.business.delete_business()
        business = Business.objects.all()
        self.assertTrue(len(business) > 0)
    #testing for update caption
    def test_update_metod(self):
        self.business.save_business()
        self.business.update_business()
        business = Business.objects.all()
        self.assertTrue(len(business) > 0)

class hoodproTestClass(TestCase):
    #set up method
    def setUp(self):
        self.hoodpro = hoodpro(id=9000,hoodpro_name= 'joseck')
    #testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.hoodpro,hoodpro))
    #testing for saving
    def test_save_method(self):
        self.hoodpro.save_hoodpro()
        hoodpro = hoodpro.objects.all()
        self.assertTrue(len(hoodpro) > 0)
    #testing for deleting method
    def test_delete_method(self):
        self.hoodpro.save_hoodpro()
        self.hoodpro.delete_hoodpro()
        hoodpro = hoodpro.objects.all()
        self.assertTrue(len(hoodpro) < 1)
    #testing for update caption
    def test_update_metod(self):
        self.hoodpro.save_hoodpro()
        self.hoodpro.update_hoodpro()
        hoodpro = hoodpro.objects.all()
        self.assertTrue(len(hoodpro) > 0)
    #testing for creatinging post
    def test_creation_method(self):
        self.hoodpro.create_hoodpro()
        hoodpro = hoodpro.objects.all()
        self.assertTrue(len(hoodpro) > 0)
