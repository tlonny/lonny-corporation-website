from textwrap import dedent

def get_title():
    return "The Lonny Corporation"

def get_logo_url():
    return "assets/images/lonny.png"

def get_stylesheet():
    return ("style.css")

def get_responsive_breakpoint():
    return "600px"

def get_divider_color():
    return "#3E4349"

def get_logo_dimensions():
    return (256, 256)

def get_header_logo_dimensions():
    return (32, 32)

def get_social_logo_dimensions():
    return (16, 16)

def get_social_data():
    return [
        ("Email", "mailto:t@lonny.io", "assets/images/email.svg"),
        ("Mobile", "tel:+447833387945", "assets/images/mobile.svg"),
        ("Github", "https://github.com/tlonny", "assets/images/github.svg"),
        ("Discord", "https://discord.gg/S5UzdS3rEF", "assets/images/discord.svg"),
    ]

def get_project_data():
    return [
        (
            "Lonny Corporation Website Repo", 
            "https://github.com/tlonny/lonny-corporation-website", 
            "The code to build this static website. Written entirely in python :-)"
        ),

        (
            "A sensible Neovim configuration",
            "https://github.com/tlonny/nvim-config",
            "This config is written entirely in lua. It has all the good stuff you'd expect: LSP, Nvimtree, Copilot, Trouble, Lualine, Bufferline, Telescope etc."
        )
    ]
