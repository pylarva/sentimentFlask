from pro_flask import app, db
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    # manager.run()
    app.run(debug=True, host='0.0.0.0', port=3010)