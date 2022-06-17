from flask_app import db


class User(db.Document):
    active = db.BooleanField(default=False)

    # User authentication information
    password = db.StringField()
    email = db.StringField()
    user_id = db.StringField()
    address = db.StringField()

    # User information
    first_name = db.StringField(default='')
    last_name = db.StringField(default='')

    # Relationships
    roles = db.StringField()
    email_confirmed_at = db.DateTimeField()

    def get_email(self):
        return self.email

    def get_user_id(self):
        return self.user_id