from ..models.parent import ParentOtpModel
from random import randint


def send_verification_code(parent, student):
    code = randint(1000, 9999)
    ParentOtpModel.objects.update_or_create(parent=parent, student=student, defaults={"code": code})
    print("code: ", code)
    return code
