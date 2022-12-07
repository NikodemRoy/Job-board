from django.test import TestCase
from django.contrib.auth import get_user_model

class CustomUserTest(TestCase):
    def test_create_user(self):
        CustomUser = get_user_model()
        password="TestPassing123!"
        email="test@test.com"
        user = CustomUser.objects.create_user(email=email, password=password)

        self.assertEqual(user.email, "test@test.com")
        self.assertTrue(user.check_password(password))
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        CustomUser = get_user_model()
        password="TestPassing123!"
        email="test@test.com"
        admin_user = CustomUser.objects.create_superuser(email=email, password=password)
        self.assertEqual(admin_user.email, "test@test.com")
        self.assertTrue(admin_user.check_password(password))
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
