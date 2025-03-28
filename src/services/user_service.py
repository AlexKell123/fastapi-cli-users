class UserService:
    def __init__(self, repository, notification, er_handler):
        self._repository = repository
        self._notification = notification
        self._error_handler = er_handler

    def create(self, full_name: str, email: str):
        if self.check_email_duplicate(email):
            return self._error_handler.duplicate_found("email", email)
        result = self._repository.create(full_name, email)
        self.send_invite_notification(email, full_name)
        return result

    def read(self, user_id: int):
        return self._repository.read(user_id)

    def update(self, user_id: int, full_name: str, email: str):
        if self.check_email_duplicate(email, current_key=user_id):
            return self._error_handler.duplicate_found("email", email)
        return self._repository.update(user_id, full_name, email)

    def delete(self, user_id: int):
        return self._repository.delete(user_id)

    def check_email_duplicate(self, email, current_key=None):
        return self._repository.read_by_email(email, current_key)

    def send_invite_notification(self, email, full_name):
        msg = f"Пользователь {full_name} добавлен в базу"
        self._notification.send(msg, email)

