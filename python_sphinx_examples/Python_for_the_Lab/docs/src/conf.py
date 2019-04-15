# -*- coding: utf-8 -*-
import os
import sys

sys.path.insert(0, os.path.abspath('../..'))
extensions = [
    'sphinx.ext.autodoc', 
    'sphinx.ext.viewcode']

project = 'My Other Module'
copyright = 'This work is supported by the US Goverment'
author = 'Johnathon Gard'
version = ''
release = '0.1'
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
pygments_style = 'sphinx'
html_theme = 'classic'
html_static_path = ['_static']
