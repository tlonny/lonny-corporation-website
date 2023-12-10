from lonnycorp.lib.dom import style

@style
def style_shims():
    return lambda cls: """
        body {
            margin: 0px;
            font-family: monospace;
            font-size: 0.9rem;
            color: #3E4349;
        }

        a {
            color: #004B6B;
            text-decoration: underline;
        }

        a:hover {
            color: #722f80;
        }

        h1 {
            color: #3E4349;
            font-size: 1.2rem; 
        }

        h2 {
            color: #3E4349;
            font-size: 1.1rem; 
        }

        h3 {
            color: #3E4349;
            font-weight: bold;
        }

        pre code {
            white-space: pre-wrap;
            overflow-wrap: anywhere;
            font-size: 1rem;
        }

        p code, li code {
            background-color: #F0F0F0;
        }

        p {
            margin: 0; padding: 0;
        }
    """

def meta(doc, *, title):
    doc.style(style_shims())
    doc.tag("link", {"rel" : "icon", "type" : "image/x-icon", "href" : "/assets/images/favicon.png"})
    doc.tag("meta", {"name": "viewport", "content" : "width=device-width, initial-scale=1.0"})
    with doc.tag("title"):
        doc.text(title)