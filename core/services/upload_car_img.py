import os.path

import uuid

from core.dataclasses.car_dataclass import CarDataClass


def upload_car_img(instance: CarDataClass, filename: str) -> str:
    ext = filename.split('.')[-1]
    return os.path.join('cars', instance.brand, str(instance.id), 'image', f'{uuid.uuid1()}.{ext}')
