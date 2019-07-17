class Order:
    def __init__(self, user_id: int, status: str = 'new'):
        self.user_id = user_id
        self.status = status

    def set_status(self, new_status: str):
        if new_status not in ('new', 'paid', 'confirmed', 'shipped'):
            raise ValueError(f'{new_status} is not a correct status!')

        self.status = new_status
