from html import escape
from textwrap import indent, dedent
from functools import wraps

indent_prefix = " " * 4
mark = object()

class TextNode:
    def __init__(self, text):
        self.text = text

    def render(self):
        yield (0, escape(self.text))

class RawNode:
    def __init__(self, raw):
        self.html = raw
    
    def render(self):
        yield (0, self.html)

class DOMNode:
    def __init__(self, parent, tag_name, attrs):
        self.parent = parent
        self.children = list()
        self.tag_name = tag_name
        self.attributes = attrs

    def __enter__(self):
        self.document.parent_stack.append(self)

    def __exit__(self, exc_type, exc_value, traceback):
        self.document.parent_stack.pop()

    @property
    def document(self):
        return self.parent.document

    def render(self):
        fmtted_attrs = " ".join(f"{k}=\"{v}\"" for k, v in self.attributes.items())
        yield (0, f"<{self.tag_name} {fmtted_attrs}>" if len(fmtted_attrs) > 0 else f"<{self.tag_name}>")
        for child in self.children:
            for indent_count, line in child.render():
                yield (indent_count + 1, line)
        yield (0, f"</{self.tag_name}>")

class Document(DOMNode):
    def __init__(self):
        super().__init__(None, "html", dict())
        self.parent_stack = list()
        self.unique_id_gen = 0
        self.style_class_names = dict()

        with self:
            self.head = self.tag("head")
            self.body = self.tag("body")
        with self.head:
            self.auto_style = self.tag("style", {"id" : "dreamlink-auto-style"})


    def get_parent(self):
        return self.parent_stack[-1] if len(self.parent_stack) > 0 else self

    def tag(self, tag, attrs = dict()):
        parent = self.get_parent()
        tag_node = DOMNode(parent, tag, attrs)
        parent.children.append(tag_node)
        return tag_node

    def text(self, text):
        parent = self.get_parent()
        parent.children.append(TextNode(text))

    def raw(self, raw):
        parent = self.get_parent()
        parent.children.append(RawNode(raw))

    def attr(self, attr_name, attr_value):
        parent = self.get_parent()
        parent.attributes[attr_name] = attr_value

    def style(self, style_template):
        cache_key, style_lambda = style_template
        if cache_key not in self.style_class_names:
            class_name = f"cls-{self.unique_id_gen}"
            self.unique_id_gen += 1
            self.style_class_names[cache_key] = class_name
            with self.auto_style:
                rendered_template = style_lambda(class_name)
                self.raw(dedent(rendered_template).strip())
        return self.style_class_names[cache_key]

    @property
    def document(self):
        return self

    def __str__(self):
        return "\n".join([
            "<!DOCTYPE html>",
            * (indent(line, indent_prefix * indent_count) for indent_count, line in self.render())
        ])

def style(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        cache_key = (
            fn.__module__,
            fn.__name__,
            *args,
            mark,
            *kwargs.items()
        )
        return (cache_key, fn(*args, **kwargs))
    return wrapper