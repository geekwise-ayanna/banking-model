from django.db import models

class Product(models.Model):
  loan_options = (
      ('student', 'STUDENT'),
      ('home', 'HOME'),
      ('car', 'CAR'),
  )

  loan_type = models.CharField(
      max_length=10,
      choices=loan_options,
      default=loan_options[0],
  )

  loan_balance = models.CharField(max_length=12)

  amount_due = models.CharField(max_length=10)

  def __str__(self):
    return(f"{self.pk} | Loan Type: {self.loan_type} | Loan Balance: {self.loan_balance}")