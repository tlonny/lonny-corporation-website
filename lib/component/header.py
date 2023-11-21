from dominate import tags
from dominate.util import text
from lib.style import style
from lib.component.social_icon import social_icon
from lib.component.vertical_divider import vertical_divider
from lib.config import (
    get_title,
    get_logo_url,
    get_header_logo_dimensions,
    get_social_data,
    get_responsive_breakpoint
)

def header_title():
    class_name = style(lambda cls: f"""
        .{cls} {{
            display: flex;
            flex-direction: row;
            gap: 12px;
            justify-content: flex-start;
            align-items: center;
            font-size: 1rem;
            font-weight: bold;
            padding: 10px;
        }}
    """)

    width, height = get_header_logo_dimensions()
    img_url = get_logo_url()
    with tags.div(cls=class_name):
        tags.img(src=img_url, width=width, height=height)
        text(get_title())

def social_bar():
    class_name = style(lambda cls: f"""
        .{cls} {{
            display: flex;
            flex-direction: row;
            justify-content: center;
            padding: 10px;
            gap: 24px;
        }}

        @media(min-width: {get_responsive_breakpoint()}) {{
            .{cls} {{
                display: none;
            }}
        }}
    """)
    with tags.div(cls=class_name):
        for _, href, icon_url in get_social_data():
            social_icon(href = href, icon = icon_url)

def header():
    class_name = style(lambda cls: f"""
        .{cls} {{
            display: flex;
            flex-direction: column;
            margin-bottom:25px;
            width: 100%;
        }}
    """)
    with tags.div(cls=class_name):
        header_title()
        vertical_divider()
        social_bar()
