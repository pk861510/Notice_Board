from django.db import models

# Create your models here.

class Notice(models.Model):
    DEPARTMENT_CHOICES = [('exam', 'Examination'),
                          ('sport', 'Sports'),
                          ('clubs', 'Student Clubs')
                          
                          #Add other departments            
                          ]
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    department = models.CharField(max_length=50,choices=DEPARTMENT_CHOICES)
    date_posted = models.DateTimeField(auto_now_add = True)
    pdfs = models.FileField(upload_to='notices/pdfs/' , blank=True, null=True)

    def __str__(self):
        return self.title