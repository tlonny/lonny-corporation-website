from dominate import tags
from dominate.util import text
from lib.config import get_social_logo_dimensions
from lib.style import style

def project_link(title, *, description, href):
    class_name = style(lambda cls: f"""
        .{cls} {{
            display: flex;
            flex-direction: column;
            justify-contents: left;
        }}

        .{cls} a {{
            font-weight: bold;
            font-size: 1rem;
        }}
    """)

    with tags.div(cls=class_name):
        tags.a(title, href = href)
        text(description)