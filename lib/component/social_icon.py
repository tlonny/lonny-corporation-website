from dominate import tags
from lib.config import get_social_logo_dimensions

def social_icon(*, icon, href):
    width, height = get_social_logo_dimensions()
    with tags.a(href=href):
        tags.img(src=icon, width=width, height=height)