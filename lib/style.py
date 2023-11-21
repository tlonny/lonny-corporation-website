from hashlib import md5
from typing import Callable
from textwrap import dedent

class StyleSheet:
    def __init__(self):
        self.style_fragments = dict()
        self.previously_bound_sheet = None

    def add_style(self, css):
        if isinstance(css, Callable):
            null_hash = md5(css("").encode("utf-8")).hexdigest()
            class_name = f"cls-{null_hash}"
            css = css(class_name)
        else:
            class_name = None

        css = dedent(css)
        hash = md5(css.encode("utf-8")).hexdigest()
        if hash not in self.style_fragments:
            self.style_fragments[hash] = css
        return class_name

    def __str__(self):
        return "\n".join(self.style_fragments.values())

    def __enter__(self):
        self.previous_bound_sheet = StyleSheet.bound_sheet
        StyleSheet.bound_sheet = self
        return

    def __exit__(self, _type, _value, _traceback):
        StyleSheet.bound_sheet = self.previous_bound_sheet
        return

    bound_sheet = None

def style(css):
    if StyleSheet.bound_sheet is None:
        raise Exception("No stylesheet is bound")
    return StyleSheet.bound_sheet.add_style(css)