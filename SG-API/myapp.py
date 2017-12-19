from app import create_app, db
from app.db import User, Role
from flask_script import Shell, Manager

app = create_app('default')

manager = Manager(app)

def make_shell_context():
    return dict(db=db, User=User, Role=Role)
manager.add_command("shell", Shell(make_context=make_shell_context))
    
if __name__ == '__main__':
    manager.run()
    