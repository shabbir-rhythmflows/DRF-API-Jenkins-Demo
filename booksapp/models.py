from django.db import models

# Create your models here
    
class Post(models.Model):
    title = models.CharField(max_length = 80)
    content = models.CharField(max_length = 300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class APILogsModel2(models.Model):
   id = models.BigAutoField(primary_key=True)
   api = models.CharField(max_length=1024, help_text='API URL')
   headers = models.TextField()
   body = models.TextField()
   method = models.CharField(max_length=10, db_index=True)
   client_ip_address = models.CharField(max_length=50)
   response = models.TextField()
   status_code = models.PositiveSmallIntegerField(help_text='Response status code', db_index=True)
   execution_time = models.DecimalField(decimal_places=5, max_digits=8,
                                       help_text='Server execution time (Not complete response time.)')
   added_on = models.DateTimeField()
   
   def __str__(self):
      return self.api

   class Meta:
      db_table = 'drf_api_logs2'
      verbose_name = 'API Log'
      verbose_name_plural = 'API Logs'