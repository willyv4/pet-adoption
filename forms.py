from argparse import OPTIONAL
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, RadioField, SelectField
from wtforms.validators import InputRequired, URL, Optional, NumberRange, AnyOf


class AddPetForm(FlaskForm):

    name = StringField("Pet Name", validators=[
                       InputRequired(message='Name is required')])
    species = StringField("Species", validators=[
                          InputRequired(message='Species is required'), AnyOf(['cat', 'dog', 'bird', 'porcupine', 'Cat', 'Dog', 'Bird', 'Porcupine', 'CAT', 'DOG', 'BIRD', 'PORCUPINE'], message="Please enter a Cat, Dog, Bird, or Porcupine")])
    photo_url = StringField("Photo URL", validators=[
                            Optional(), URL(message="Please enter a proper URL")])
    age = IntegerField("Age", validators=[NumberRange(
        min=0, max=30)])
    notes = StringField("Notes")
