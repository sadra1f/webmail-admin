from django.db import models


class EmailAccount(models.Model):
    user = models.CharField(max_length=200, help_text="The E-Mail address")
    password = models.CharField(max_length=200)

    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_on"]
