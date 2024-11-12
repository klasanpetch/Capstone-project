from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
class MenuViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user)
        self.menu_item_1 = Menu.objects.create(title="Salad" , price=5.99)
        self.menu_item_2 =Menu.objects.create(title="Burger" , price=8.99)
        self.menu_item_3 =Menu.objects.create(title= "Pizza", price=12.99)
        self.client = APIClient()
    def test_getall(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.get('/restaurant/menu/')
        expected_data = MenuSerializer([self.menu_item_1,self.menu_item_2, self.menu_item_3], many=True).data
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, expected_data)