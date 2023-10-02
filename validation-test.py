# This code will use Pydantic for testing
# import pydantic
import json
import string
from typing import Optional

import pydantic
from pydantic import (
    BaseModel,
    FieldValidationInfo,
    ValidationError,
    field_validator,
)


class User(BaseModel):
    username: str
    password: str
    age: int
    score: float
    email: Optional[str]
    phone_number: Optional[str]\



    @field_validator('email', 'phone_number')
    @classmethod
    def validate_phone_or_email(cls, values):
        if 'email' in values or 'phone_number' in values:
            return values
        else:
            raise ValueError("Need either an email or phone_number")


    @field_validator('username')
    @classmethod
    def username_is_valid(cls, value):
        if len(value) < 8:
            raise ValueError("The password must be a length of 8 characters")

        if any(p in value for p in string.punctuation):
            if any(d in value for d in string.digits):
                if any(l in value for l in string.ascii_lowercase):
                    if any(u in value for u in string.ascii_uppercase):

                        raise ValueError("The password needs at least one punctuation symbol, digit, uppercase and "
                                         "lowercase character")

    @field_validator('age', 'score')
    @classmethod
    def valid_number(cls, value):
        if value >= 0:
            return value
        else:
            raise ValueError("Number must be positive")


user1 = User(username='jefe85', password='password',
             age=25, score=109)

print(user1)
print(user1.score)

json_users = [User(**u) for u in json.loads(open("users.json"))]
