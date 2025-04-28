from abc import ABC, abstractmethod

# Абстрактный класс для уведомлений
class Notification(ABC):
    @abstractmethod
    def send(self, message: str):
        pass

# Конкретный класс для отправки уведомлений через Email
class EmailNotification(Notification):
    def send(self, message: str):
        return f"Email sent: {message}"

# Конкретный класс для отправки уведомлений через SMS
class SMSNotification(Notification):
    def send(self, message: str):
        return f"SMS sent: {message}"

# Порождающий паттерн "Фабричный метод" для создания уведомлений
class NotificationFactory:
    def create_notification(self, notification_type: str) -> Notification:
        if notification_type == "email":
            return EmailNotification()
        elif notification_type == "sms":
            return SMSNotification()
        else:
            raise ValueError(f"Unknown notification type: {notification_type}")
