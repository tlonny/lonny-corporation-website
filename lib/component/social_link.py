from dominate import tags
from lib.config import get_social_logo_dimensions
from lib.style import style

def social_link(title, *, icon, href):
    class_name = style(lambda cls: f"""
        .{cls} {{
            display: flex;
            flex-direction: row;
            gap: 12px;
            align-items: center;
            justify-content: left;
        }}
    """)

    width, height = get_social_logo_dimensions()
    with tags.div(cls=class_name):
        tags.img(src=icon, width=width, height=height)
        tags.a(title, href = href)




