class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


emails = list()


while True:
    command = input().split(' ')
    if command[0] == 'Stop':
        break

    sender = command[0]
    receiver = command[1]
    content = command[2]
    email = Email(sender, receiver, content)
    emails.append(email)

numbers = list(map(int, input().split(', ')))
send_email = [emails[x].send() for x in numbers]

for email in emails:
    print(email.get_info())