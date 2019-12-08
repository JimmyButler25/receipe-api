from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTest(TestCase):

    def test_create_user_with_email_successful(self):
        """test creating new user with an email is successful"""
        email = "okidijimmyjones@gmail.com"
        password = "test@123"
        user = get_user_model().objects.create_user(email = email,
        password = password
        )

        """testing the email and password. password test we use assertTrue"""
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))


