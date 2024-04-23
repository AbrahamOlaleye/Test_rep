import re
import argparse
import sys

class Email:
    """
    A class to store data related to an individual email message.

    Attributes:
        message_id (str): Unique identifier for the email.
        date (str): Date when the email was sent.
        subject (str): Subject line of the email.
        sender (str): Email address of the sender.
        receiver (str): Email address of the receiver.
        body (str): Text content of the email body.

    Parameters:
        message_id (str): ID of the message.
        date (str): Sending date of the email.
        subject (str): Subject of the email.
        sender (str): Sender's email address.
        receiver (str): Receiver's email address.
        body (str): Body of the email.
    """
    def __init__(self, message_id, date, subject, sender, receiver, body):
        self.message_id = message_id
        self.date = date
        self.subject = subject
        self.sender = sender
        self.receiver = receiver
        self.body = body

class Server:
    """
    A class to store and process multiple Email objects from a file.

    Attributes:
        emails (list of Email): List of Email objects representing each email in the file.

    Parameters:
        path (str): Path to the file containing email data.
    """
    def __init__(self, path):
        self.emails = []
        with open(path, 'r') as file:
            data = file.read()
            emails_raw = data.split(" End Email")
            for email_content in emails_raw:
                if email_content.strip():  # Avoid processing empty strings
                    self.emails.append(self.parse_email(email_content))
    
    def parse_email(self, content):
        """
        Parses individual email content into an Email object using regular expressions.

        Parameters:
            content (str): Raw content of a single email from the file.

        Returns:
            Email: An instance of the Email class containing parsed data.
        """
        message_id = re.search(r'Message-ID: (.+)', content)
        date = re.search(r'Date: (.+)', content)
        subject = re.search(r'Subject: (.+)', content)
        sender = re.search(r'From: (.+)', content)
        receiver = re.search(r'To: (.+)', content)
        body = re.search(r'X-FileName: .*\n\n([\s\S]*)', content)

        return Email(
            message_id.group(1) if message_id else "No Message ID Found",
            date.group(1) if date else "No Date Found",
            subject.group(1) if subject else "",
            sender.group(1) if sender else "No Sender Found",
            receiver.group(1) if receiver else "No Receiver Found",
            body.group(1).strip() if body else "No Body Found"
        )

def parse_args(args_list):
    """
    Parses command line arguments.

    Parameters:
        args_list (list of str): Arguments provided via the command line.

    Returns:
        argparse.Namespace: Contains the namespace with command-line arguments.
    """
    parser = argparse.ArgumentParser(description="Process some emails.")
    parser.add_argument('path', type=str, help='the path to the email text file')
    return parser.parse_args(args_list)

def main(path):
    """
    Main function that processes the email file and reports the number of processed emails.

    Parameters:
        path (str): Path to the file containing the emails.

    Returns:
        int: Number of emails processed.
    """
    server = Server(path)
    return len(server.emails)

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    print("Number of emails processed:", main(args.path))
