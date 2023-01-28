from django.db import models
    
    
class Employee(models.Model):
    emp_name = models.CharField('Employee Name', max_length=100)
    month = models.DateField("Month")
    iteam_count = models.IntegerField("Iteam Count")
    
    def __str__(self):
        return self.emp_name
    
    

CHOICES =(
    ("Numbers", "Numbers"),
    ("Meter", "Meter"),
    ("KG", "KG"),
    ("Kilo Meter", "Kilo Meter"),
)
class Iteams(models.Model):
    
    iteam_code = models.IntegerField("Iteam Code")
    iteam_name = models.CharField("Iteam Name",max_length=40)
    iteam_mes_para = models.CharField("Messure",choices=CHOICES ,default="Numbers",max_length=40)
    iteam_qty = models.IntegerField("Iteam Qty")
    image = models.ImageField(upload_to='images/')
    supplier_name = models.CharField("Supplier Name",max_length=40)
    employee_name = models.ForeignKey(Employee, default=1, verbose_name="emp_name", on_delete=models.SET_DEFAULT)
    created_on = models.DateTimeField('Created', auto_now_add=True)

    class Meta:
        ordering = ['iteam_name']

    def __str__(self):
        return self.iteam_name
        
    def get_absolute_url(self):
        return reverse('product_edit', kwargs={'pk': self.pk})