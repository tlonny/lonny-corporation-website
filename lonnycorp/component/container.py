from contextlib import contextmanager
from lonnycorp.lib.dom import style
from lonnycorp.config import get_max_width_breakpoint
from lonnycorp.component.header import header
from lonnycorp.component.nav import nav_column

@style
def container_style():
    return lambda cls: f"""
        .{cls} {{
            width: 100%;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            align-items: center;
        }}
    """

@style
def container_body_style():
    return lambda cls: f"""
        .{cls} {{
            display: flex;
            flex-direction: column;
            max-width: 840px;
            width: 100%;
            justify-content: center;
            height: 100%;
        }}

        @media(max-width: {get_max_width_breakpoint()}) {{
            .{cls} {{
                justify-content: flex-start;
            }}
        }}
    """

@style
def container_columns_style():
    return lambda cls: f"""
        .{cls} {{
            display: flex;
            flex-direction: row;
            gap: 24px;
        }}
    """

@style
def container_content_style():
    return lambda cls: f"""
        .{cls} {{
            display: flex;
            flex-direction: column;
            width: 100%;
            padding: 12px;
            gap: 12px;
        }}
    """

@contextmanager
def container(doc):
    with doc.tag("div", {"class" : doc.style(container_style())}):
        header(doc)
        with doc.tag("div", {"class" : doc.style(container_body_style())}):
            with doc.tag("div", {"class" : doc.style(container_columns_style())}):
                nav_column(doc)
                with doc.tag("div", {"class" : doc.style(container_content_style())}):
                    yield