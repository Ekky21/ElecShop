import unittest
from notification_service.notification import NotificationService

class TestNotificationService(unittest.TestCase):
    def test_send_notification(self):
        service = NotificationService()
        self.assertEqual(service.send_notification("Order has been placed"), "Notification sent: Order has been placed")

if __name__ == '__main__':
    unittest.main()
