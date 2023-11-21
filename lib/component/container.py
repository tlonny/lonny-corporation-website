from dominate import tags
from contextlib import contextmanager

from lib.style import style
from lib.component.header import header
from lib.config import get_responsive_breakpoint

def container_content():
    class_name = style(lambda cls: f"""
        .{cls} {{
            display: flex;
            flex-direction: column;
            justify-content: center;
            height: 100%;
        }}

        @media(max-width: {get_responsive_breakpoint()}) {{
            .{cls} {{
                justify-content: flex-start;
            }}
        }}
    """)

    return tags.div(cls=class_name)

@contextmanager
def container():
    class_name = style(lambda cls: f"""
        .{cls} {{
            width: 100%;
            height: 100vh;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
        }}
    """)

    with tags.div(cls=class_name):
        header()
        with container_content():
            yield