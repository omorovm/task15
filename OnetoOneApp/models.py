from django.db import models

# Create your models here.

class Brain(models.Model):
    iq = models.IntegerField()
    weight = models.IntegerField()


class Human(models.Model):
    SEX = (
        ('male', 'мужской'),
        ('female', 'женский'),
        ('think', 'неопределенный'),
        ('fight helicopter', 'боевой вертолет')
    )
    name = models.CharField(max_length=40, default='John')
    sex = models.CharField(max_length=20, choices=SEX)
    brain = models.OneToOneField(
        Brain,
        on_delete=models.CASCADE,
        related_query_name = 'human'
        )
# >>> from OnetoOneApp.models import Brain, Human
# >>> brain1 = Brain.objects.create(iq=110, weight=2)
# >>> human1 = Human.objects.create(sex='male', brain=brain1)
# >>> human1.brain
# <Brain: Brain object (1)>
# >>> brain1.human
# <django.db.models.fields.related_descriptors.create_reverse_many_to_one_manager.<locals>.RelatedManager object at 0x7f74b1934970>
# >>> brain1.human.all()
# <QuerySet [<Human: Human object (1)>]>
# >> brain1.iq = 150
# >>> brain1.save()
