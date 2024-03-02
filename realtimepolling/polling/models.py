from django.db import models

class Poll(models.Model):
  question=models.CharField(max_length=200, verbose_name='Poll Question')
  pub_date=models.DateTimeField('date published')

  def __str__(self):
    return self.question
  
class Choice(models.Model):
  poll=models.ForeignKey(Poll,on_delete=models.CASCADE,verbose_name='Related poll')
  choice_text=models.CharField(max_length=200,verbose_name='Choice text')
  votes=models.IntegerField(default=0,verbose_name='Number of votes')

  def __str__(self):
    return self.choice_text