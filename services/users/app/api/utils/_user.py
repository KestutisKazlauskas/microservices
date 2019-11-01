import re
from app.api.exceptions import ValidationError
from app.api.models import User

class UserManger:

    _model = User

    def __init__(self, _db, data, required=None):
        self._db = _db
        self._raw_data = data
        self._validated_data = {}

        if not required:
            self._required = ["email", "username"]

        self.error = False
        self.data = {}

    def _validate_email(self, email):
        # Make a regular expression
        # for validating an Email
        regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
        if not re.search(regex, email):
            raise ValidationError("email is not valid!")

        user = self._model.query.filter_by(email=email).first()

        if user:
            raise ValidationError("user exists!")


    def _validate_required(self, fields):
        for field in fields:
            if not self._raw_data.get(field):
                raise ValidationError(f"{field} is required!")

    def is_valid(self):
        try:
            self._validate_required(self._required)
            self._validate_email(self._raw_data.get('email'))
        except ValidationError as error:
            self.error = error.message

            return False

        self._validated_data = self._raw_data

        return True

    def save(self):
        if self._validated_data:
            user = self._model(
                email=self._validated_data.get('email'),
                username=self._validated_data.get('username')
            )
            self._db.session.add(user)
            self._db.session.commit()

            self.data = {
                "id": user.id,
                "email": user.email,
                "username": user.username
            }

