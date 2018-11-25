from flask_wtf import FlaskForm

from wtforms import StringField, TextAreaField, SubmitField, RadioField, TextField

from wtforms.validators import Required, Email, ValidationError

from ..models import Subscriber


class CommentForm(FlaskForm):
    """
    class to create comment form
    """
    name = StringField('Your Name')
    comment = TextField('Write your comment')
    submit = SubmitField('Submit')


class BlogForm(FlaskForm):
    """
    class to create blog post form
    """
    header = StringField('Blog post title')
    post = TextAreaField('Blog Content')
    category = RadioField('Categories', choices = [('foodlab', 'foodlab'),('recipes', 'recipes'),('techniques', 'techniques'), ('equipment','equipment')],validators=[Required()])
    submit = SubmitField('Submit')


class SubscriptionForm(FlaskForm):
    username = StringField('Your Name Please', validators=[Required()])
    email = StringField('Your Email',validators=[Required(), Email()])
    submit = SubmitField('Subscribe')

    def validate_email(self,data_field):
                if Subscriber.query.filter_by(email=data_field.data).first():
                    raise ValidationError('There is an account with that email')

class UpdateProfile(FlaskForm):
    """
    class update profile to create form
    """
    bio = TextAreaField('Tell Us Something Interesting About You')
    submit = SubmitField('Submit')