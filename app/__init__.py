import os
from flask import Flask, render_template, url_for
from config import Config
from flask_migrate import Migrate
from app.dbcon import db
from flask_login import LoginManager


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)


    # inittialize database   
    db.init_app(app)


    #initialize login manager
    login_manager = LoginManager()
    login_manager.login_view = 'users_bp.login'
    login_manager.login_message_category = 'info'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return Users.query.get(int(user_id))

    # initialize migration
    migrate = Migrate(app, db)


    # import all models from Models directory
    from app.models.users import Users
    from app.models.products import Products
    from app.manage_users.form import LoginForm 


    # register blueprints
    from app.manage_users.routes import users_bp
    app.register_blueprint(users_bp)
    from app.manage_product.routes import product_bp
    app.register_blueprint(product_bp)
    from app.manage_purchase.routes import purchase_bp
    app.register_blueprint(purchase_bp)
    from app.manage_issue.routes import issue_bp
    app.register_blueprint(issue_bp)


    @app.route('/')
    def index():
        return render_template('main.html')

    return app


#from app import create_app




