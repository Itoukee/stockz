class User:
    def __init__(self, user_id: int, name: str):
        self.id = user_id
        self.name = name

    def update_name(self, new_name: str):
        self.name = new_name
