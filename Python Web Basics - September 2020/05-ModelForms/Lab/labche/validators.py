from django.core.validators import MinValueValidator

page_validator = MinValueValidator(1, 'Please provide valid number')
