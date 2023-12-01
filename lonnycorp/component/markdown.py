from markdown import markdown as _markdown

def markdown(doc, *, markdown):
    doc.raw(_markdown(markdown))