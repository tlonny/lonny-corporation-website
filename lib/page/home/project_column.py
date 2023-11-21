from dominate import tags

from lib.style import style
from lib.component.project_link import project_link
from lib.config import (
    get_project_data
)

def project_column():
    class_name = style(lambda cls: f"""
        .{cls} {{
            display: flex;
            flex-direction: column;
            max-width: 800px;
            padding: 12px;
            gap: 15px;
        }}
    """)
    with tags.div(cls=class_name):
        for title, href, description in get_project_data():
            project_link(
                title,
                href = href,
                description = description
            )