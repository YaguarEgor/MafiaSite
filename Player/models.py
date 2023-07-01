from django.db import models

# from phonenumber_field.modelfields import PhoneNumberField

from django.contrib.auth.models import AbstractUser


class CustomPlayer(AbstractUser):
    
    # """telephone = models.CharField(verbose_name="Телефон", max_length=20, default = "+7 (547) 221-87-98") # TODO: Отлавливать повторяющиеся номеры при обработке формы
    # birthday = models.DateField(verbose_name="Дата рождения", null=True, blank=True, default = "2000-09-12")
    # photo = models.ImageField(verbose_name="Фотография", null=True, blank=True)"""

    # first_name = models.CharField(
    #     verbose_name="First name", max_length=50, default="hd"
    # )
    # last_name = models.CharField(verbose_name="Last name", max_length=50, default="hd2")
    # username = models.CharField(
    #     verbose_name="Username", max_length=50, default="hd", unique=True
    # )
    
    def __str__(self):
        return self.username

    # class Meta:
    #     verbose_name = "игрок"
    #     verbose_name_plural = "игроки" 
    


    
