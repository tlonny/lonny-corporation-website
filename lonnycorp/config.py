from textwrap import dedent

default_title = "The Lonny Corporation"

def get_title():
    return "The Lonny Corporation"

def get_logo_url():
    return "/assets/images/lonny.png"

def get_favicon_url():
    return "/assets/images/favicon.png"

def get_breakpoint():
    return 768

def get_max_width_breakpoint():
    return f"{get_breakpoint()}px"

def get_min_width_breakpoint():
    return f"{get_breakpoint() + 1}px"

def get_divider_color():
    return "#3E4349"

def get_logo_dimensions():
    return (256, 256)

def get_header_logo_dimensions():
    return (32, 32)

def get_social_logo_dimensions():
    return (24, 24)