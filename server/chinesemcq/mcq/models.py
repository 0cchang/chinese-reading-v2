from django.db import models

#each character has its own unique id answer
class SingleCharacterQuestion(models.Model):
    chinese_word = models.CharField(max_length=1)
    pinyin = models.CharField(max_length=10)
    english = models.CharField(max_length=200)
    answer = models.IntegerField()

    def __str__(self):
        return f"{self.chinese_word} {self.pinyin} {self.english}"
    
class omegaCharacter(models.Model):
    character = models.CharField(max_length=1, unique = True)
    unique_id = models.IntegerField(unique=True)

    def __str__(self):
        return f'{self.character} -> {self.unique_id}'

