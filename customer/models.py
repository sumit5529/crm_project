from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    gst_number = models.CharField(max_length=15)
    reminder_frequency = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    


# class EmailContent(models.Model):
#     recipient_email = models.EmailField()
#     message_text = models.TextField()

#     def __str__(self):
#         return self.recipient_email  # Display recipient email in admin panel

