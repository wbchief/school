
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Shell
from schoolspider import create_app, db
from schoolspider.models import Login
from schoolspider.main.view import app
#app = create_app('production')
manager = Manager(app)
migrate = Migrate(app, db)

def make_shell_context():
    return dict(app=app, db=db, School=Login)

manager.add_command('shell', Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
