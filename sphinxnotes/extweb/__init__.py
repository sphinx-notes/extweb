# -*- coding: utf-8 -*-
"""
    sphinxnotes.extweb
    ~~~~~~~~~~~~~~~~~~

    Sphinx extension for embedding external web resources (like video, music, etc)

    :copyright: Copyright 2022 by the Shengyu Zhang.
    :license: BSD, see LICENSE for details.
"""

from typing import List
from docutils import nodes
from urllib.parse import urlencode
from importlib.metadata import version

from sphinx.util import logging
from sphinx.util.docutils import SphinxDirective

__title__= 'sphinxnotes-extweb'
__license__ = 'BSD'
__version__ = '1.0a0'
__author__ = 'Shengyu Zhang'
__url__ = 'https://sphinx-notes.github.io/extweb'
__description__ = 'Sphinx extension for embedding external web resources (like video, music, etc)'
__keywords__ = 'documentation, sphinx, web, video, music'

logger = logging.getLogger(__name__)

class bilibili_node(nodes.General, nodes.Element): pass

class BilibiliDirective(SphinxDirective):
    required_arguments = 1

    def run(self) -> List[nodes.Node]:
        node = bilibili_node()
        node['docname'] = self.env.docname
        node['rawtext'] = self.block_text
        node['bvid'] = self.arguments[0]
        return [node]

def html_visit_bilibili_node(self, node:bilibili_node):
    src = '//player.bilibili.com/player.html?' + urlencode({
        'bvid': node['bvid'],
    })
    style = 'width: 100%; height: 500px; max-width: 100%；align:center; padding:20px 0;'
    self.body.append(self.starttag(node, 'iframe',
                                   SRC=src,
                                   SCROLLING='no',
                                   BORDER='0',
                                   FRAMEBORDER='no',
                                   FRAMESPACING='0',
                                   ALLOWFULLSCREEN='true',
                                   STYLE=style,
                                   CLASS='extweb'))
    self.body.append('</iframe>')
    raise nodes.SkipNode

def setup(app):
    app.add_node(bilibili_node, html=(html_visit_bilibili_node, None))
    app.add_directive('bilibili', BilibiliDirective)

    return {'version': version('sphinxnotes.extweb')}
