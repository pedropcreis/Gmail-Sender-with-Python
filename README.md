# Gmail Sender

By Pedro Reis (pedropcr.42@gmail.com)

Made using Python and the smtplib library.

This is a simple project in portuguese for sending text emails with your Gmail account. I choose Gmail because it's one of the most used email services in the world. However, if you change where is written:
domain = smtplib.SMTP('smtp.gmail.com', 587)
and put:
domain = smtplib.SMTP('smtp.name_of_the_email_service_you_want', 587)
it will allow you to use the email service that you prefer.

Before you start using this program, be assured that the 'access to less secure app' option is activated on your Gmail account settings. This will give the program permission to use your email address and password to log on in your account and send the emails.

Since it's necessary to have access to the internet, maybe sometimes the program won't be able to send the emails, depending on your internet conection.

Feel free to use this Gmail Sender!
