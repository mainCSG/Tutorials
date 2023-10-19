# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

import os
import sys
# import time

sys.path.insert(0, os.path.abspath('../..'))
# print(os.path.abspath('../../qudipy'))
# print(os.path.abspath('../../tutorials'))

# from pathlib import Path
# path = Path(os.getcwd())

# # update base working directory to Tutorials
# if path.stem != 'Tutorials':
#     # print(path.parents[0])

#     # move 2-directories up
#     base_dir = path.parents[1]
#     include_path = os.path.join(base_dir, 'qudipy')
#     # os.chdir(base_dir)
#     sys.path.insert(0, include_path)
# else:
#     base_dir = path
#     include_path = os.path.join(base_dir, 'qudipy')
#     sys.path.insert(0, include_path)

# print(os.path.abspath('../..'))
# print(include_path)

# for i in range(10,0,-1):
#     sys.stdout.write(str(i)+' ')
#     sys.stdout.flush()
#     time.sleep(1)


# sys.path.insert(0, os.path.abspath('../../notebooks'))
# sys.path.insert(0, os.path.abspath('../../markdown'))

# -- Project information -----------------------------------------------------

project = 'QuDiPy Simulator'
copyright = '2023, Zach D. Merino'
author = 'Zach D. Merino'

# The full version, including alpha/beta/rc tags
release = 'Oct. 11th 2023'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = ['sphinx.ext.autodoc',
              'sphinx.ext.todo',
              'sphinx.ext.doctest',
              'sphinx.ext.napoleon',
              'nbsphinx',
              'myst_parser']

# tell sphinx what different file extensions should associated with
source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}

todo_include_todos = True
napoleon_google_docstring = False
napoleon_include_special_with_doc = False
nbsphinx_allow_errors = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
