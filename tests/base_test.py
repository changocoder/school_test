from unittest import TestCase

from alembic import command
from alembic.config import Config

from app.app_factory import initialize_app
from app.config import TestConfig
from app.extension import db


class ShcoolDBTest(TestCase):

    def create_app(self):
        return initialize_app(TestConfig)

    def setUp(self):
        self.app = self.create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.app.testing = True
        self.client = self.app.test_client()
        self.headers = {
            'Content-Type': 'application/json'
        }
        self.session = db.session
        self.alembic_config = Config(TestConfig.ALEMBIC_INI_PATH)
        command.upgrade(self.alembic_config, 'head')

    def tearDown(self):
        if self.session:
            self.session.remove()
        command.downgrade(self.alembic_config, 'base')
        db.Model.metadata.drop_all(db.engine)
        self.app_context.pop()
