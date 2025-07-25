#
# Pygments documentation build configuration file
#

import os
import re
import sys

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.insert(0, os.path.abspath('..'))

# ruff: noqa: E402
import pygments
import pygments.formatters
import pygments.lexers
import pygments.styles
import tests.contrast.test_contrasts as test_contrasts

# -- General configuration -----------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.intersphinx', 'pygments.sphinxext']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'Pygments'
copyright = '2006-2024, Georg Brandl and Pygments contributors'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = pygments.__version__
# The full version, including alpha/beta/rc tags.
release = version

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
exclude_patterns = ['_build']

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
#pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []


# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'pygments14'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
html_theme_path = ['_themes']

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = 'Pygments'

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = '_static/favicon.ico'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
html_sidebars = {'index': ['indexsidebar.html', 'searchbox.html']}

# Additional templates that should be rendered to pages, maps page names to
# template names.
html_additional_pages = {
    'styles': 'styles.html',
    }

if os.environ.get('WEBSITE_BUILD'):
    html_additional_pages['demo'] = 'demo.html'
    html_static_path.append('_build/pyodide')

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'Pygments'


# -- Options for LaTeX output --------------------------------------------------

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
#'papersize': 'letterpaper',

# The font size ('10pt', '11pt' or '12pt').
#'pointsize': '10pt',

# Additional stuff for the LaTeX preamble.
#'preamble': '',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
    ('docs/index', 'Pygments.tex', 'Pygments Documentation',
     'Pygments authors', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

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
    ('docs/index', 'pygments', 'Pygments Documentation',
     ['Pygments authors'], 1)
]

# If true, show URL addresses after external links.
#man_show_urls = False


# Example configuration for intersphinx: refer to the Python standard library.
#intersphinx_mapping = {'http://docs.python.org/': None}

rst_prolog = f'.. |language_count| replace:: {len(list(pygments.lexers.get_all_lexers()))}'

def pg_context(app, pagename, templatename, ctx, event_arg):
    # casting string to bool doesn't work, we'll use 0 to disable
    ctx['demo_active'] = os.environ.get('WEBSITE_BUILD')  != '0'

    if pagename == 'demo':
        ctx['lexers'] = sorted(pygments.lexers.get_all_lexers(plugins=False), key=lambda x: x[0].lower())

    if pagename in ('styles', 'demo'):
        with open('examples/example.py', encoding='utf-8') as f:
            html = f.read()
        lexer = pygments.lexers.get_lexer_for_filename('example.py')
        min_contrasts = test_contrasts.min_contrasts()
        ctx['styles_aa'] = []
        ctx['styles_sub_aa'] = []
        # Use STYLE_MAP directly so we don't get plugins as with get_all_styles().
        for style in pygments.styles.STYLE_MAP:
            if not pygments.styles.get_style_by_name(style).web_style_gallery_exclude:
                aa = min_contrasts[style] >= test_contrasts.WCAG_AA_CONTRAST
                bg_r, bg_g, bg_b = test_contrasts.hex2rgb(pygments.styles.get_style_by_name(style).background_color)
                ctx['styles_aa' if aa else 'styles_sub_aa'].append(
                    dict(
                        name=style,
                        html=pygments.highlight(
                            html,
                            lexer,
                            pygments.formatters.HtmlFormatter(noclasses=True, style=style),
                        ),
                        # from https://en.wikipedia.org/wiki/Relative_luminance
                        bg_luminance=(0.2126*bg_r + 0.7152*bg_g + 0.0722*bg_b)
                    )
                )

        # sort styles according to their background luminance (light styles first)
        # if styles have the same background luminance sort them by their name
        def sortkey(s):
            return (-s['bg_luminance'], s['name'])
        # the default style is always displayed first
        default_style = ctx['styles_aa'].pop(0)
        ctx['styles_aa'].sort(key=sortkey)
        ctx['styles_aa'].insert(0, default_style)
        ctx['styles_sub_aa'].sort(key=sortkey)


def source_read(app, docname, source):
    # linkify issue / PR numbers in changelog
    if docname == 'docs/changelog':
        with open('../CHANGES', encoding='utf-8') as f:
            changelog = f.read()

        idx = changelog.find('\nVersion 2.4.2\n')

        def linkify(match):
            url = 'https://github.com/pygments/pygments/issues/' + match[1]
            return f'`{match[0]} <{url}>`_'

        linkified = re.sub(r'(?:PR)?#([0-9]+)\b', linkify, changelog[:idx])
        source[0] = linkified + changelog[idx:]


def setup(app):
    app.connect('html-page-context', pg_context)
    app.connect('source-read', source_read)
