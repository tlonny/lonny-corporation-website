from dominate import document, tags
from os import symlink
from os.path import exists, abspath

from lib.style import StyleSheet
from lib.component.container import container
from lib.component.default_style import default_style
from lib.page.home import home

from lib.config import (
    get_title,
    get_stylesheet,
    get_favicon_url
)

def build():
    style = StyleSheet()
    doc = document(title = get_title())
    style_dst = get_stylesheet()

    with doc.head:
        tags.link(rel="stylesheet", href=style_dst)
        tags.link(rel="icon", href=get_favicon_url())
        tags.meta(name="viewport", content="width=device-width, initial-scale=1")
    with doc.body, style:
        default_style()
        with container():
            home()

    with open("build/index.html", "w") as f:
        f.write(str(doc))
    with open(f"build/{style_dst}", "w") as f:
        f.write(str(style))

    if not exists("build/assets"):
        symlink(abspath("assets"), abspath("build/assets"))

if __name__ == "__main__":
    build()
