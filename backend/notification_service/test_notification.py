import unittest
from notification import NotificationFactory, EmailNotification, SMSNotification


class TestNotificationFactory(unittest.TestCase):

    def test_create_email_notification(self):
        # Тестируем создание уведомления через email
        factory = NotificationFactory()
        notification = factory.create_notification("email")

        # Проверяем, что созданный объект является экземпляром EmailNotification
        self.assertIsInstance(notification, EmailNotification)
        self.assertEqual(notification.send("Test Email"), "Email sent: Test Email")

    def test_create_sms_notification(self):
        # Тестируем создание уведомления через SMS
        factory = NotificationFactory()
        notification = factory.create_notification("sms")

        # Проверяем, что созданный объект является экземпляром SMSNotification
        self.assertIsInstance(notification, SMSNotification)
        self.assertEqual(notification.send("Test SMS"), "SMS sent: Test SMS")

    def test_create_notification_invalid_type(self):
        # Тестируем создание уведомления с неверным типом
        factory = NotificationFactory()

        # Проверяем, что при неправильном типе выбрасывается исключение ValueError
        with self.assertRaises(ValueError):
            factory.create_notification("push")


if __name__ == "__main__":
    unittest.main()
