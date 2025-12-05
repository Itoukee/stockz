from domain.user.entity import User

mock_values = {
    "DEFAULT_ID": 1,
    "DEFAULT_MAIL": "noooo@broo.com",
    "PATCH_MAIL": "non@gmail.com",
}


def update_email():
    user = User(
        id=mock_values["DEFAULT_ID"], email=mock_values["DEFAULT_MAIL"], password=""
    )
    user.update_email(mock_values["PATCH_MAIL"])

    assert user.email == mock_values["PATCH_MAIL"]
