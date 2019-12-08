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

    """test to make email case insensitive when a new user registers"""
    def test_new_user_email_normalized(self):
        """Test the email for new user is normalized"""
        email = 'okidijimmyjones@GMAIL.COM'
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())

# run the program >docker-compose run app sh -c 'python manage.py test'


    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

# run the test, which fails