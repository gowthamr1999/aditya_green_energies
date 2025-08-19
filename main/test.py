from django.core.mail import send_mail

subject = 'Test Email'
message = 'This is a test email sent using SMTP in Django.'
from_email = 'your-email@example.com'
recipient_list = ['gowthamreddy19999@gmail.com']

send_mail(subject, message, from_email, recipient_list)
print('hello')

# import ssl
# from django.core.mail import get_connection, send_mail

# ssl_context = ssl._create_unverified_context()

# connection = get_connection(
#     host="smtp.gmail.com",
#     port=587,
#     username="info@adityagreenenergies.com",
#     password="cjqnrffezlzalgfg",
#     use_tls=True,
#     ssl_context=ssl_context
# )

# send_mail(
#     "Test Mail",
#     "Hello from Django!",
#     "info@adityagreenenergies.com",
#     ["gowthamreddy19999@gmail.com"],
#     connection=connection
# )
