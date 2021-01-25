from django.db import models
from django.contrib.auth.models import User


class Employee(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    drinks = models.BooleanField(help_text="Este funcionário irá beber?")
    guest = models.BooleanField(blank=True)
    guest_drink = models.BooleanField(blank=True)

    def __str__(self):
        return self.user.username


class Barbeque(models.Model):
    COLAB_VALUE = 20
    organized_by = models.CharField(max_length=70, blank=True)
    participants = models.ManyToManyField(Employee)
    _date = models.DateField(blank='true')

    def __str__(self):
        return self.organized_by + "'s BBQ" if self.organized_by else ""

    def getColabValue(self):
        return self.COLAB_VALUE

    def getOrganizer(self):
        return self.organized_by

    def setColabValue(self, value):
        self.COLAB_VALUE = value

    def getParticipants(self):
        return self.participants.all()

    def getGuests(self):
        guests = 0
        for participant in self.getParticipants():
            if participant.guest:
                guests += 1
        return guests

    def getFoodAmount(self):
        total_participants = self.participants.count() + self.getGuests()
        return self.COLAB_VALUE * total_participants

    def getDrinkAmount(self):
        total = 0
        for participant in self.getParticipants():
            if participant.drinks:
                total += 1
            if participant.guest_drink:
                total += 1
        return self.COLAB_VALUE * total

    def totalAmount(self):
        return self.getFoodAmount() + self.getDrinkAmount()
