from lonnycorp.lib.dom import style
from lonnycorp.config import get_divider_color

@style
def divider_style():
    return lambda cls: f"""
        .{cls} {{
            width: 100%;
            border-bottom: 1px dotted {get_divider_color()};
        }}
    """

def divider(doc):
    class_name = doc.style(divider_style())
    return doc.tag("div", {"class" : class_name})



