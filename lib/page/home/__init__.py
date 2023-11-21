from dominate import tags
from lib.style import style

from .social_column import social_column
from .project_column import project_column

def home():
    class_name = style(lambda cls: f"""
        .{cls} {{
            display: flex;
            gap: 20px;
            flex-direction: row;
        }}
    """)
    with tags.div(cls=class_name):
        social_column()
        project_column()