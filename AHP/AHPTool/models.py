from django.db import models
from django.template.defaultfilters import default

# Create your models here.
class Dimension(models.Model):
    name = models.CharField(max_length = 200)
    
    def __unicode__(self):
        return self.name
    
class Rating(models.Model):
    Scale = (
             (9,9),
             (8,8),
             (7,7),
             (6,6),
             (5,5),
             (4,4),
             (3,3),
             (2,2),
             (1,1),
             )
    Dim1 = models.ForeignKey(Dimension, related_name='dim1_+')
    Dim2 = models.ForeignKey(Dimension, related_name = 'dim2_+')
    rating = models.IntegerField(choices = Scale, default= 1)
    date =  models.DateTimeField(auto_now=True)
    sessionkey = models.CharField(max_length = 200)
    
    def __unicode__(self):
        return "%s zu %s: %s" %(self.Dim1.name,self.Dim2.name, self.rating)
    