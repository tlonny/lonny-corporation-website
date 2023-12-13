from pdoo import style
from lonnycorp.component.nav import nav_links
from lonnycorp.component.divider import divider
from lonnycorp.config import (
    get_title,
    get_logo_url,
    get_header_logo_dimensions,
    get_min_width_breakpoint
)

@style
def header_title_style():
    return lambda cls: f"""
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
    """

@style
def social_bar_style():
    return lambda cls: f"""
        .{cls} {{
            display: flex;
            flex-direction: row;
            justify-content: center;
            padding: 10px;
            gap: 24px;
        }}
    """

@style
def header_style():
    return lambda cls: f"""
        .{cls} {{
            display: flex;
            flex-direction: column;
            width: 100%;
        }}

        @media(min-width: {get_min_width_breakpoint()}) {{
            .{cls} {{
                display: none;
            }}
        }}
    """

def header_title(doc):
    class_name = doc.style(header_title_style())
    width, height = get_header_logo_dimensions()
    img_url = get_logo_url()
    with doc.tag("div", {"class" : class_name}):
        with doc.tag("a", {"href" : "/"}):
            doc.tag("img", {"src" : img_url, "width" : width, "height" : height})
        with doc.tag("div"):
            doc.text(get_title())

def social_bar(doc):
    class_name = doc.style(social_bar_style())
    with doc.tag("div", {"class" : class_name}):
        nav_links(doc)

def header(doc):
    class_name = doc.style(header_style())
    with doc.tag("div", {"class" : class_name}):
        header_title(doc)
        divider(doc)
        social_bar(doc)
