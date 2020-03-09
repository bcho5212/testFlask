from flask_wtf import Form
from wtforms import StringField, RadioField, IntegerField, SubmitField


class VendorDetailsForm(Form):
    vendor_name = RadioField("Name of Vendor", choices=[
        ('LB+MOR', 'LB+MOR'),
        ('TDC+MOR', 'TDC+MOR'),
        ('LB+LQS', 'LB+LQS'),
        ('TDC+LQS', 'TDC+LQS'),
        ('MOR-only', 'MOR-only')
    ])
    languages = StringField("Relevant Languages")
    project_type = RadioField("Project Type", choices=[
        ('M', 'Marketing'),
        ('P', 'Product')
    ])
    new_words = IntegerField("Number of New Words")
    submit = SubmitField("Submit")
