from typing import Optional


class User:
    def __init__(self, user_id: Optional[int], name: str):
        self.id = user_id
        self.name = name

    def update_name(self, new_name: str):
        self.name = new_name

    def to_dict(self):
        return {"id": self.id, "name": self.name}
