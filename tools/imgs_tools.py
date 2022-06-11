from PIL import Image
from images.images import add_text


def make_health_condition_pic(head, body, arm_l, arm_r, leg_l, leg_r):
    image = Image.open('/images/health_condition/bg.png')
    add_text(image, )
    image.save('/images/health_condition.png')
    pass