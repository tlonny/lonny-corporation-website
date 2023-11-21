from lib.style import style

def style_body():
    style("""
        body {
            margin: 0px;
            color: #3E4349;
        }
    """)

def style_anchors():
    style("""
        a {
            color: #004B6B;
            text-decoration: underline;
            text-decoration-style: dotted;
        }

        a:hover {
            color: #722f80;
        }
    """)

def default_style():
    style_body()
    style_anchors()
