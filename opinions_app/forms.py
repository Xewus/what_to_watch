from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, URLField
from wtforms.validators import DataRequired, Length, Optional, URL


class OpinionForm(FlaskForm):
    title = StringField(
        label='Введите название фильма',
        validators=(
            DataRequired('Обязательное поле'),
            Length(1, 128)
        )
    )
    text = TextAreaField(
        label='Напишите мнение',
        validators=(
            DataRequired('Обязательное поле'),
        )
    )
    source = URLField(
        label='Добавьте ссылку на подробный обзор фильма',
        validators=(
            URL(message='Некорректный URL'),
            Length(1, 256),
            Optional()
        )
    )
    added_by = StringField(
        label='Автор мнения',
        validators=(
            Length(1, 64),
            Optional()
        )
    )
    submit = SubmitField(
        'Добавить',
    )
