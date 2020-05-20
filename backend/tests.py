from django.test import TestCase
from .models import *
# Create your tests here.


class LoginModuleTests(TestCase):

    def test_existed_user_register(self):

        users = User.objects.all()
        for user in users:
            data = {'user_name': user.user_name, 'user_email': user.user_email, 'user_password': 'test'}
            response = self.client.post('/login/register/', data)
            self.assertContains(response, "Email Already Exist!")

    def test_login_with_wrong_password(self):

        users = User.objects.all()
        for user in users:
            data = {'user_name': user.user_name, 'user_email': user.user_email, 'user_password': 'ukisdhfauiweblbasdl'}
            response = self.client.post('/login/verify/', data)
            self.assertContains(response, "Wrong Password!")

    def test_login_with_wrong_user_email(self):

        users = User.objects.all()
        for user in users:
            data = {'user_name': user.user_name, 'user_email': 'xxxxxxx@xxxxxx.com', 'user_password': 'ukisdhfauiweblbasdl'}
            response = self.client.post('/login/verify/', data)
            self.assertContains(response, "Email incorrect!")

    def test_correct_login(self):

        users = User.objects.all()
        for user in users:
            data = {'user_name': user.user_name, 'user_email': user.user_email, 'user_password': user.user_password}
            response = self.client.post('/login/verify/', data)
            self.assertContains(response, "Login Successfully!")

    def test_register_with_strange_password_and_user_name(self):

        data = {'user_name': 'new_test_user_][1@#1', 'user_email': 'a_@testing_email', 'user_password': 'ajshd@#$&!@#wer2[]a;s'}
        response = self.client.post('/login/register/', data)
        self.assertContains(response, "Signup Successfully!")

    def test_register_with_long_password(self):

        data = {'user_name': 'new_test_user_name', 'user_email': 'a_testing_email',
                'user_password': 'ajshdfui!@#wer2[]a;sajksdhfjkalksdjfklajsdklflahiuhqwuiebuifabdijpojiosdjoa'}
        response = self.client.post('/login/register/', data)
        self.assertContains(response, "Password Should Not Longer Than 30 Characters!")


