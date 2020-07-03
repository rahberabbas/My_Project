from django.db import models

# Create your models here.
class Context(models.Model):
    num = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 100, default="")
    cat = models.CharField(max_length = 100, default="")
    desc = models.CharField(max_length = 1000, default = "")
    pub_date = models.DateField()
    img = models.ImageField(upload_to = "prone/images", default="")
    vide = models.FileField(upload_to='prone/videos', null=True, verbose_name="")

    def __str__(self):
        return self.name + ": " + str(self.vide)
