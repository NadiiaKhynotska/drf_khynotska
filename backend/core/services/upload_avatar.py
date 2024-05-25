import os.path

import uuid

from core.dataclasses.user_dataclass import ProfileDataClass


def upload_avatar(instance: ProfileDataClass, filename: str) -> str:
    ext = filename.split('.')[-1]
    return os.path.join('users', instance.name, 'avatar', f'{uuid.uuid1()}.{ext}')
