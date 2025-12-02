from typing import Optional


class User:
    def __init__(self, user_id: Optional[int], email: str, password: str):
        self.id = user_id
        self.email = email
        self.password = password

    def update_email(self, new_email: str):
        self.email = new_email

    def to_dict(self):
        return {"id": self.id, "email": self.email}

    def __str__(self) -> str:
        return f"id:{self.id}, email :{self.email}"
