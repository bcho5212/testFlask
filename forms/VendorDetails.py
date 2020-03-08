from flask_wtf import Form
from wtforms import StringField, RadioField, IntegerField


class VendorDetailsForm(Form):
    name = StringField("Name of Vendor")
    languages = StringField("Relevant Languages")
    project_type = RadioField("Project Type", choices=[('M', 'Marketing'), ('P', 'Product')])
    new_words = IntegerField("Number of New Words")
