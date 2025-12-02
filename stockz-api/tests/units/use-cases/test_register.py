from domain.user.use_cases import CreateUserUseCase
from domain.user.entity import User

test_user = {"id": 1, "email": "toto@gmail.com", "password": "123456"}


def test_register_user(mocker):
    mock_repo = mocker.Mock()
    mock_repo.create.return_value = User(user_id=None, **test_user)

    uc = CreateUserUseCase(mock_repo)

    user = uc.execute(email=test_user["email"], password=test_user["password"])

    assert user.id == test_user["id"]
    assert user.email == test_user["email"]
    mock_repo.create.assert_called_once()
