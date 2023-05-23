# coding:utf-8
import re
import panflute as pf

def action(elem, doc):
    if isinstance(elem, pf.Link):
        matches = list(re.finditer(r'(\.md)', elem.url))
        if matches:
            m = matches[-1]
            elem.url = elem.url[:m.start(1)] + '.html' + elem.url[m.end(1):]
            return elem
        matches = list(re.finditer(r'(\.ipynb)', elem.url))
        if matches:
            m = matches[-1]
            elem.url = elem.url[:m.start(1)] + '.html' + elem.url[m.end(1):]
            return elem

if __name__ == '__main__':
    pf.run_filter(action)