from apps import create_app
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from exts import db
from apps.insulator.model import *

app = create_app()
migrate = Migrate(app=app, db=db)
manager = Manager(app=app)
manager.add_command('db', MigrateCommand)
# print(app.url_map)

if __name__ == '__main__':
    manager.run()
