from django.db import models

class Label(models.Model):
    key = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.key

class Translation(models.Model):
    label = models.ForeignKey(Label, related_name='translations', on_delete=models.CASCADE)
    language_code = models.CharField(max_length=10)
    text = models.TextField()

    class Meta:
        unique_together = ('label', 'language_code')
