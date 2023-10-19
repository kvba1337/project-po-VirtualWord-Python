class NotificationManager:
    def __init__(self):
        self.notifications = []

    def addNotification(self, notification: str):
        self.notifications.append(notification)

    def clear(self):
        self.notifications = []

    def printOutNotifications(self) -> str:
        out = ""
        for notification in self.notifications:
            out += f"{notification}\n"

        return out
