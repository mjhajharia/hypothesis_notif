from h_notify import *
import time
import os
import traceback

default_token = os.environ.get("default_token")
default_smtp_server = os.environ.get("default_smtp_server")
default_email_sender = os.environ.get("default_email_sender")
default_email_password = os.environ.get("default_email_password")
group_id = os.environ.get("group_id")
recipient_email = os.environ.get("recipient_email")
recipient_email2 = os.environ.get("recipient_email2")

group_name = os.environ.get("group_name")

notify_email_group_activity(group=group_id, groupname=group_name, token=default_token, pickle=f"private_files/{group_id}", smtp=default_smtp_server, sender=default_email_sender, sender_password=default_email_password, recipient=recipient_email, recipient2=recipient_email2)