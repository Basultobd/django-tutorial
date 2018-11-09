from django.db import models

# Create your models here.
class Question(models.Model):

    class Meta:
        db_table = 'question'

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

class Choice(models.Model):

    class Meta:
        db_table = 'choice'

    # each choice is associated with a question
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes_count = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
