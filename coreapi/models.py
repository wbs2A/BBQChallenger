from django.db import models


class Guest(models.Model):
    name = models.CharField(max_length=70)
    drinks = models.BooleanField(help_text="Este convidado irá beber?")

    class Meta:
        verbose_name_plural = "Guests"

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=70)
    drinks = models.BooleanField(help_text="Este funcionário irá beber?")
    guests = models.ManyToManyField(Guest, blank=True)

    def __str__(self):
        return self.name if self.name else 'Nome não informado'


class Barbeque(models.Model):
    COLAB_VALUE = 20
    organized_by = models.CharField(max_length=70, blank=True)
    participants = models.ManyToManyField(Employee)

    def __str__(self):
        return self.organized_by+"'s BBQ" if self.organized_by else ""

    def getColabValue(self):
        return self.COLAB_VALUE

    def setColabValue(self, value):
        self.COLAB_VALUE = value

    def totalAmount(self):
        pass

    def getParticipants(self):
        pass

    def getGuests(self):
        pass

    def getFoodAmount(self):
        pass

    def getDrinkAmount(self):
        pass

