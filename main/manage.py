from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from main import db, app

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()

# python manage.py db init -> running this cmd inside docker container will create migrations
# python manage.py db migrate -> will migrate