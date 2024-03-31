from app.school.blueprints.user.models import User
from app.school.blueprints.utils import GenericService


class UserService(GenericService):
    _model = User

    def get_by_field(self, field, value):
        return self._session.query(self._model).filter(getattr(self._model, field) == value).first()

    def get_by_email(self, email):
        return self.get_by_field("email", email)

