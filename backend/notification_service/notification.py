class NotificationService:
    _instance = None
    
    def __new__(cls):
        if not cls._instance:
            cls._instance = super(NotificationService, cls).__new__(cls)
        return cls._instance
    
    def send_notification(self, message):
        return f"Notification sent: {message}"
