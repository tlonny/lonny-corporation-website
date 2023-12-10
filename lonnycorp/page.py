from lonnycorp.lib.dom import style, Document
from lonnycorp.config import default_title
from lonnycorp.component.meta import meta
from lonnycorp.component.container import container
from lonnycorp.component.markdown import markdown

@style
def project_style():
    return lambda cls: f"""
        .{cls} {{
            display: flex;
            flex-direction: column;
            justify-contents: left;
        }}

        .{cls} a {{
            font-weight: bold;
            font-size: 1rem;
        }}
    """

def project(doc, *, title, href, description):
    class_name = doc.style(project_style())
    with doc.tag("div", {"class" : class_name}):
        with doc.tag("a", {"href" : href}):
            doc.text(title)
        with doc.tag("div"):
            markdown(doc, markdown = description)

def page():
    doc = Document()
    with doc.head:
        meta(doc, title = default_title)
    with doc.body:
        with container(doc):
            with doc.tag("h1"):
                doc.text("Projects")

            project(
                doc,
                title = "Doors",
                href = "#",
                description = "A _free-to-play_ creation/exploration game. Create and upload levels with cusotm assets. Link them together with doors and explore a seamless, interconnected and often non-euclidian dreamscape.",
            )

            project(
                doc,
                title = "Lonny Corporation website generator",
                href = "https://github.com/tlonny/lonny-corporation-website",
                description = "The code to build this static website. Written entirely in python :-)",
            )

            project(
                doc,
                title = "A sensible Neovim configuration",
                href = "https://github.com/tlonny/nvim-config",
                description = "A sensible Neovim configuration loaded with all the good stuff you'd expect - lspconfig, treesitter, copilot, nvimtree, etc.",
            )
    return str(doc)