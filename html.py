import sys
from HTMLParser import HTMLParser


class TagStripper(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.reset()
        self.fed = []

    def handle_data(self, d):
        self.fed.append(d)

    def get_data(self):
        return ' - '.join(self.fed)


def strip_tags(html):
    s = TagStripper()
    s.feed(html)
    return s.get_data()


if len(sys.argv) < 2:
    # fname = 'help.txt'
    # with open(fname, 'r') as fin:
    print 'usage: python html.py <file>'
    sys.exit()
        

text = str('')
f = sys.argv[1]
with open(f, 'r') as fin:
    text += fin.read()
print 'Text = ' + strip_tags(text)
