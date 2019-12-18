from django.db import models

class Account(models.Model):
  type_options = (
      ('checking', 'CHECKING'),
      ('savings', 'SAVINGS'),
      ('credit', 'CREDIT'),
  )

  account_name = models.CharField(max_length=40)

  account_type = models.CharField(
      max_length=10,
      choices=type_options,
      default=type_options[0],
  )

  account_balance = models.CharField(max_length=12)

  def __str__(self):
    return(f"{self.pk} | Account Name: {self.account_name} | Account Type: {self.account_type} ")
