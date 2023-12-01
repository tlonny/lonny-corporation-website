from os import symlink, makedirs
from os.path import exists, abspath, dirname
from lonnycorp.page import page

def build():
    if not exists("build/assets"):
        symlink(abspath("assets"), abspath("build/assets"))
    build_path = "build/index.html"
    makedirs(dirname(build_path), exist_ok = True)
    with open(build_path, "w") as f:
        f.write(page())

if __name__ == "__main__":
    build()
