# from django.test import SimpleTestCase, Client
# from django.urls import reverse
# from showroom.models import Customer, Products, Booking, Manufacturer, Car, Accesories, UserMessage
# import json

# class TestViews(SimpleTestCase):


#     def test_signup_GET(self):
#         client = Client()
#         response = client.get(reverse('signup'))
#         self.assertEquals(response.status_code, 200)
#         self.assertTemplateUsed(response, 'showroom/signup.html')
    
#     def test_login_GET(self):
#         client = Client()
#         response = client.get(reverse('login'))
#         self.assertEquals(response.status_code, 200)
#         self.assertTemplateUsed(response, 'showroom/login.html')

#     def test_search_GET(self):
#         client = Client()
#         response = client.get(reverse('search'))
#         self.assertEquals(response.status_code, 200)
#         self.assertTemplateUsed(response, 'showroom/search.html')

#     def test_profile_GET(self):
#         client = Client()
#         response = client.get(reverse('profile'))
#         self.assertEquals(response.status_code, 200)
#         self.assertTemplateUsed(response, 'showroom/profile.html')

