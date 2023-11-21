from dominate import tags
from lib.config import get_divider_color
from lib.style import style

def vertical_divider():
    class_name = style(lambda cls: f"""
        .{cls} {{
            width: 100%;
            border-bottom: 1px dotted {get_divider_color()};
        }}
    """)
    return tags.div(cls=class_name)




