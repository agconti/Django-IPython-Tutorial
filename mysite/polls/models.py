from django.db import models
#add support for timezones
import datetime
from django.utils import timezone

class Poll(models.Model):
    #Our new custom method
    def was_published_recently(self):
            return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
        
    def __unicode__(self):
        return self.question   
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):    
    def __unicode__(self):
        return self.choice_text    
    poll = models.ForeignKey(Poll)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)