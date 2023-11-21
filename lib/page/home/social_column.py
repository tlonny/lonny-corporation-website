from dominate import tags

from lib.style import style
from lib.component.social_link import social_link
from lib.component.vertical_divider import vertical_divider
from lib.config import (
    get_logo_url,
    get_logo_dimensions,
    get_social_data,
    get_responsive_breakpoint
)

def social_column():
    class_name = style(lambda cls: f"""
        .{cls} {{
            display: flex;
            flex-direction: column;
            padding: 12px;
            gap: 12px;
        }}

        @media(max-width: {get_responsive_breakpoint()}) {{
            .{cls} {{
                display: none;
            }}
        }}
    """)
    width, height = get_logo_dimensions()
    img_url = get_logo_url()
    with tags.div(cls=class_name):
        tags.img(src=img_url, width=width, height=height)
        vertical_divider()
        for title, href, icon_url in get_social_data():
            social_link(
                title,
                href = href,
                icon = icon_url
            )