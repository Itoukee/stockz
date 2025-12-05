from typing import Optional
from pydantic import BaseModel


class User(BaseModel):
    id: Optional[int] = None
    email: str
    password: str

    def update_email(self, new_email: str):
        self.email = new_email

    def to_dict(self):
        return {"id": self.id, "email": self.email}

    def __str__(self) -> str:
        return f"id:{self.id}, email :{self.email}"
