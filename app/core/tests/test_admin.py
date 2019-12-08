from django.test import TestCase, Client
from django.contrib.auth import get_user_model
# helper function called reverse to generate url for our page
from django.urls import reverse

class AdminSiteTests(TestCase):
    """Create a setup function"""
    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email = 'admin@gmail.com',
            password = 'password123'
            
        )
        # this uses the client helper function to log a user into django with django auth which makes our tests easier to write
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email = 'test@gmail.com',
            password = 'pass123',
            name = 'Test user full name'
        )

    def test_users_listed(self):
        """Test for users listed on User page"""
        url = reverse('admin:core_user_changelist')
        response = self.client.get(url)

        self.assertContains(response, self.user.name)
        self.assertContains(response, self.user.email)

    # run the test

    def test_user_change_page(self):
        """Check that the user edit page works"""
        url = reverse('admin:core_user_change', args=[self.user.id])
        # similar to /admin/core/user/1
        response = self.client.get(url)

        # test that the page renders okay
        self.assertEqual(response.status_code, 200)
    # test fails when we run it

    def test_create_user_page(self):
        """Test to check that the user page works"""
        url = reverse('admin:core_user_add')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    # run the test bse we have not yet specified user name