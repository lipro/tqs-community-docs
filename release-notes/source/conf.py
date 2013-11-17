# -*- coding: utf-8 -*-
#
# TQ Systems Community BSP Release Notes documentation build configuration file, created by
# sphinx-quickstart on Mon Oct 28 15:32:22 2013.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys, os

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.insert(0, os.path.abspath('.'))

# -- General configuration -----------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = ['sphinx.ext.todo', 'sphinxcontrib.email', 'sphinxcontrib.blockdiag', 'sphinxcontrib.tikz']

# Choose the image processing, either 'Netpbm' or 'ImageMagick'. The default is 'Netpbm'.
tikz_proc_suite = 'ImageMagick'

# Enable/disable transparent graphics. The default is True.
tikz_transparent = True

# Add some <string> to the sub process LaTeX preamble for the html build target. The default is None.
# tikz_latex_preamble = ''

# Add some \usetikzlibrary{<string>} to the sub process LaTeX preamble for the html build target. The default is None.
tikz_tikzlibraries = 'arrows'

# Fontpath for blockdiag (truetype font), The default is None.
# blockdiag_fontpath = os.path.abspath('../../ressources/themes/sphinxdoc-ext/static/dejavusans_book_macroman/DejaVuSans-webfont.ttf')

# Fontmap for blockdiag (maps fontfamily name to truetype font), The default is None.
blockdiag_fontmap = os.path.abspath('../diag.fontmap')

# If this is True, blockdiag generates images with anti-alias filter. The default is False.
blockdiag_antialias = True

# You can specify image format on converting docs to HTML; accepts 'PNG' or 'SVG'. The default is 'PNG'.
blockdiag_html_image_format = 'SVG'

# You can specify image format on converting docs to TeX; accepts 'PNG' or 'PDF'. The default is 'PNG'.
blockdiag_tex_image_format = 'PDF'

# If this is True, todo and todolist produce output, else they produce nothing. The default is False.
todo_include_todos = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['../../ressources/templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'TQ Systems Community BSP Release Notes'
author = u'TQ Systems Community BSP Team'
publisher = u'Li-Pro.Net'
copyright = u'2013, ' + publisher

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '1.x'
# The full version, including alpha/beta/rc tags.
release = '1.x-current'

# A string of reStructuredText that will be included at the beginning of every
# source file that is read.
rst_prolog = '''
.. include:: /%s/docmeta.inc
.. |project| replace:: %s
.. |author| replace:: %s
.. |publisher| replace:: %s
''' % (os.path.abspath('.'),project,author,publisher)

# A string of reStructuredText that will be included at the end of every source
# file that is read. This is the right place to add substitutions that should be
# available in every file.
#rst_epilog = "\n.. include:: /%s/docrev.inc\n\n"%(os.path.abspath('.'),)

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = []

# The reST default role (used for this markup: `text`) to use for all documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []


# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'sphinxdoc-ext'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
    "sidebarwidth": 440,

    # If true, license referer is shown in the HTML footer. Default is False.
    "show_licref": True,
    "licref": "Creative Commons Attribution-ShareAlike 3.0 Unported License",
    "licref_href": "http://creativecommons.org/licenses/by-sa/3.0/",
    "licref_image": "http://i.creativecommons.org/l/by-sa/3.0/80x15.png",
    #"licref_image": "http://i.creativecommons.org/l/by-sa/3.0/88x31.png",
}

# Add any paths that contain custom themes here, relative to this directory.
html_theme_path = ['../../ressources/themes']

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = project + ' ' + release

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = "_images/lpn-logo.png"

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
#html_static_path = ['../../ressources/static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
html_sidebars = {
    '**': ['localtoc.html', 'relations.html']
}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
html_use_index = False

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False
html_copy_source = False

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = False

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'TQSystemsCommunityBSPReleaseNotesdoc'


# -- Options for LaTeX output --------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    'papersize': 'a4paper',

    # The font size ('10pt', '11pt' or '12pt').
    'pointsize': '11pt',

    # Additional stuff for the LaTeX preamble.
    'inputenc': '',
    'utf8extra': '',
    'preamble': '''

\usepackage{tikz}
\usepackage{pgfplots}
\usetikzlibrary{arrows}
\usepackage{fontspec}
\setmainfont{DejaVu Sans Condensed}
\setsansfont{DejaVu Sans Condensed}
\setmonofont{DejaVu Sans Mono}
\setromanfont{DejaVu Sans Condensed}
''',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
  ('index', 'TQSystemsCommunityBSPReleaseNotes.tex', project, author, 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
latex_logo = "_images/lpn-logo.pdf"

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True


# -- Options for manual page output --------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'tqsystemscommunitybspreleasenotes', project, [author], 7)
]

# If true, show URL addresses after external links.
#man_show_urls = False


# -- Options for Texinfo output ------------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
  ('index', 'TQSystemsCommunityBSPReleaseNotes', project,
   author, 'TQSystemsCommunityBSPReleaseNotes', 'One line description of project.',
   'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'


# -- Options for Epub output ---------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project
epub_author = author
epub_publisher = publisher
epub_copyright = copyright

# The language of the text. It defaults to the language option
# or en if the language is not set.
#epub_language = ''

# The scheme of the identifier. Typical schemes are ISBN or URL.
#epub_scheme = ''

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#epub_identifier = ''

# A unique identification for the text.
#epub_uid = ''

# A tuple containing the cover image and cover page html template filenames.
#epub_cover = ()

# HTML files that should be inserted before the pages created by sphinx.
# The format is a list of tuples containing the path and title.
#epub_pre_files = []

# HTML files shat should be inserted after the pages created by sphinx.
# The format is a list of tuples containing the path and title.
#epub_post_files = []

# A list of files that should not be packed into the epub file.
#epub_exclude_files = []

# The depth of the table of contents in toc.ncx.
#epub_tocdepth = 3

# Allow duplicate toc entries.
#epub_tocdup = True
