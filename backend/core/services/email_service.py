import os

from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from core.dataclasses.user_dataclass import UserDataClass
from core.services.jwt_service import JWTService, ActivateToken


class EmailService:
    @staticmethod
    def __send_email(to: str, template_name: str, context: dict, subject: '') -> None:
        template = get_template(template_name)
        html_content = template.render(context)
        msg = EmailMultiAlternatives(subject, from_email=os.environ.get('EMAIL_HOST_USER'), to=[to])
        msg.attach_alternative(html_content, 'text/html')
        msg.send()

    @classmethod
    def register(cls, user: UserDataClass):
        token = JWTService.create_token(user, ActivateToken)
        url = f'http://300/register/{token}'
        cls.__send_email(
            user.email,
            'register.html',
            {'name': user.profile.name, 'url': url},
            'Register'


        )
