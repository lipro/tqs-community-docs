# http://fnch.users.sourceforge.net/sphinxindexinsinglehtml.html
#
# Copyright (C) 2011 by Matteo Franchin
#
#   This file is free software: you can redistribute it and/or modify it
#   under the terms of the GNU General Public License as published
#   by the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This file is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   A copy of the GNU General Public License is available at
#   <http://www.gnu.org/licenses/>.

from sphinx.util.compat import Directive
from sphinx.builders.html import SingleFileHTMLBuilder
from docutils import nodes
from docutils.parsers.rst import directives

class globaltoc(nodes.General, nodes.Element):
    pass

def visit_globaltoc_node(self, node):
    self.body.append(node['content'])

def depart_globaltoc_node(self, node):
    pass

class GlobalTocDirective(Directive):
    required_arguments = 0
    optional_arguments = 1
    final_argument_whitespace = True
    option_spec = \
      {'maxdepth': directives.nonnegative_int,
       'collapse': directives.flag,
       'titlesonly': directives.flag}

    def run(self):
        node = globaltoc('')
        node['maxdepth'] = self.options.get('maxdepth', 2)
        node['collapse'] = 'collapse' in self.options
        node['titlesonly'] = 'titlesonly' in self.options
        return [node]

def process_globaltoc_nodes(app, doctree, fromdocname):
    builder = app.builder
    if builder.name != SingleFileHTMLBuilder.name:
        for node in doctree.traverse(globaltoc):
            node.parent.remove(node)

    else:
        docname = builder.config.master_doc
        for node in doctree.traverse(globaltoc):
            kwargs = dict(maxdepth=node['maxdepth'],
                          collapse=node['collapse'],
                          titles_only=node['titlesonly'])
            rendered_toctree = builder._get_local_toctree(docname, **kwargs)
            node['content'] = rendered_toctree

def setup(app):
    app.add_node(globaltoc,
                 html=(visit_globaltoc_node, depart_globaltoc_node))
    app.add_directive('globaltoc', GlobalTocDirective)
    app.connect('doctree-resolved', process_globaltoc_nodes)
