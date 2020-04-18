from django.db import models

class Product(models.Model):


	MOBILE = 'mobile'
	NOTEBOOK = 'notebook'
	TABLET = 'tablet'
	PC = 'pc'


	CHOICE_GROUP = {
		(MOBILE, 'mobile'),
		(NOTEBOOK, 'notebook'),
		(TABLET,'tablet'),
		(PC,'pc'),
	}
	
	name = models.CharField(max_length = 100)
	description = models.TextField()
	price = models.IntegerField()
	availibility = models.BooleanField(default= True)
	group = models.CharField(max_length=20, choices=CHOICE_GROUP, default=MOBILE)
	image = models.ImageField(default= 'no_image.jpg', upload_to='product_image')

	def __str__(self):
		return f'{self.name}'

# Create your models here.
