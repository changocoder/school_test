from app.models.user import User
from tests.base_test import ShcoolDBTest


class TestUser(ShcoolDBTest):
    def test_user_model_create(self):

        user = User(
            name="John",
            last_name="Doe",
            email="test@gmail.com",
            username="johndoe",
            is_active=True,
            is_admin=False,
        )
        user.set_password("123456")

        self.session.add(user)
        self.session.commit()

        user_inserted = self.session.query(User).first()

        self.assertEqual(user_inserted.name, "John")
        self.assertEqual(user_inserted.last_name, "Doe")

    def test_user_model_password(self):

        user = User(
            name="John",
            last_name="Doe",
            email="test@test.com",
            username="johndoe",
            is_active=True,
            is_admin=False,
        )

        user.set_password("123456")

        self.assertTrue(user.password)
