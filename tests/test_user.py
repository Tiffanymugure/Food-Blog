import unittest

from sqlalchemy.exc import Error

from app import Error
from app.models import User


class UserModelTest(unittest.TestCase):
    def setUp(self):
        self.new_user = User(username = 'tiff',password = '123', email = 'amiratiffany@gmail.com')

    # user saving
    def save_user(self):
        db.session.add(self.new_user)
        db.session.commit()

    # password setting test
    def test_password_setter(self):
        self.assertTrue(self.new_user.pass_secure is not None)

    # raising error when wrong password is used
    def test_no_access_password(self):
        with self.assertRaises(AttributeError):
            self.new_user.password

    # verifying password
    def test_password_verification(self):
        self.assertTrue(self.new_user.verify_password('123'))