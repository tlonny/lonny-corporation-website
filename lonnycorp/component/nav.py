from pdoo import style
from lonnycorp.component.divider import divider
from lonnycorp.config import (
    get_logo_url,
    get_logo_dimensions,
    get_max_width_breakpoint
)

@style
def header_style():
    return lambda cls: f"""
        .{cls} {{ margin: 0; width: 100%; text-align: center; }}
        .{cls} a {{ color: black; }}

    """

@style
def nav_column_style():
    return lambda cls: f"""
        .{cls} {{
            display: flex;
            flex-direction: column;
            padding: 12px;
            gap: 12px;
        }}

        @media(max-width: {get_max_width_breakpoint()}) {{
            .{cls} {{
                display: none;
            }}
        }}
    """

@style
def nav_link_style():
    return lambda cls: f"""
        .{cls} {{
            display: flex;
            flex-direction: row;
            gap: 12px;
            align-items: center;
            justify-content: left;
        }}

        @media(max-width: {get_max_width_breakpoint()}) {{
            .{cls} > *:nth-child(2) {{ display: none; }}
        }}
    """

def nav_link(doc, *, title, href, icon):
    class_name = doc.style(nav_link_style())
    with doc.tag("div", {"class" : class_name}):
        with doc.tag("a", {"href" : href}):
            doc.tag("img", {"src" : icon, "width" : 20, "height" : 20})
        with doc.tag("a", {"href" : href}):
            doc.text(title)

def nav_links(doc):
    nav_link(
        doc,
        title = "Email",
        href = "mailto:t@lonny.io",
        icon = "/assets/images/email.svg"
    )
    nav_link(
        doc,
        title = "Mobile",
        href = "tel:+447833387945",
        icon = "/assets/images/phone.svg"
    )
    nav_link(
        doc,
        title = "Github",
        href = "https://github.com/tlonny",
        icon = "/assets/images/github.svg"
    )
    nav_link(
        doc,
        title = "Discord",
        href = "https://discord.gg/S5UzdS3rEF",
        icon = "/assets/images/discord.svg"
    )
    nav_link(
        doc,
        title = "Youtube",
        href = "https://www.youtube.com/@tlonny",
        icon = "/assets/images/youtube.svg"
    )


def nav_column(doc):
    class_name = doc.style(nav_column_style())
    width, height = get_logo_dimensions()
    img_url = get_logo_url()
    with doc.tag("div", {"class" : class_name}):
        doc.tag("img", {"src" : img_url, "width" : width, "height" : height})
        with doc.tag("h1", {"class" : doc.style(header_style())}):
            with doc.tag("a", {"href" : "/"}):
                doc.text("The Lonny Corporation")
        divider(doc)
        nav_links(doc)