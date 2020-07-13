from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired


class XX_Game_Data_Form(FlaskForm):
    game_data = TextAreaField('18XX Game Data', validators=[DataRequired()])
    submit = SubmitField('Submit')
