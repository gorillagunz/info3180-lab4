from flask.ext.wtf import Form
from wtforms.fields import StringField, FileField, SelectField, IntegerField
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms.validators import Required
class ProfileForm(Form):
    image = FileField('image', validators=[])
    firstname = StringField('firstname', [Required()])
    lastname = StringField('lastname', [Required()])
    age = StringField('age', [Required()])
    sex = SelectField('sex', choices=[('M', 'Male'), ('F', 'Female')],validators=[Required()])