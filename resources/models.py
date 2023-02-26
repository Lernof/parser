from django.db import models

# Create your models here.
class Resource(models.Model):
    resource_id = models.BigAutoField(primary_key=True)
    resource_name = models.CharField(max_length=100)
    resource_url = models.CharField(max_length=255)
    top_tag = models.CharField(max_length=255)
    bottom_tag = models.CharField(max_length=255)
    title_cut = models.CharField(max_length=255)
    date_cut = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Items(models.Model):
    id = models.BigAutoField(primary_key=True)
    res_id = models.ForeignKey('Resource', on_delete=models.CASCADE)
    link = models.CharField(max_length=255)
    title = models.TextField()
    content = models.TextField()

    nd_date = models.CharField(max_length=100)
    not_date = models.CharField(max_length=100)
    s_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.res_id}'