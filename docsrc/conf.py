# Project metadata
project = "wklchris' Github Pages"
copyright = '2017, wklchris'
author = 'wklchris'
release = '2.0rc'


# Sphinx configurations
exclude_patterns = [         
    "_build"                 # Ignore _build/ to avoid recursive builds of nbsphinx
]
smartquotes = False          # Show double-dashes clearly
today_fmt = "%Y-%m-%d"       # Date format when using |today| replacement syntax
extensions = [
    'sphinx.ext.mathjax',    # Math equation support
    'recommonmark',          # Markdown support if you don't like reStructuredText
    'sphinxcontrib.bibtex',  # Bibliography support
    'nbsphinx'               # Jupyter notebook (.ipynb) file support
]

bibtex_bibfiles = ['refs.bib']
mathjax3_config = {
    'tex': {'tags': 'ams', 'useLabelIds': True},
}

html_theme = 'sphinx-simrofy-theme'

# Static paths. Folder for images, CSS, etc.
html_static_path = ["_static"]

# Load external data, if needed
try:
    import json
    with open('_static/people.json', 'r') as f:
        people_json = json.load(f)
except Exception as e:
    print(f"!Exception!: {e}")
    people_json = None
    

# Set internationalization (i18n) for multi-language support
language = 'en'
locale_dirs = ['locale/']  # This can be overwritten by sphinx-intl's "-d" arg.
gettext_compact = False

# Theme options.
# - Read sphinx_simrofy_theme/theme.conf for default values.
html_theme_options = {
    'canonical_prefix': "https://wklchris.github.io/",
    'favicon': "favicon.ico",
    'headbar_links': ['Research', 'Hobbies', 'Blog'],
    'sidebar_position': 'left',
    'github_user': 'wklchris',
    'github_repo': 'wklchris.github.io',
    # 'languages': {'en': 'English', 'zh_CN': '简体中文'},
    'logo': 'portrait.jpg',
    'logo_width': 0.75,
    'logo_radius': 0.5,
    'sidebar_home_text': f'Kanglong Wu',
    # 'sidebar_localtoc': 'collapse',
    'sidebar_toc_exclude': ['404'],
    'social_accounts': {
        'github': {'user': 'wklchris', 'url': 'https://github.com/wklchris'},
        'linkedin': {'user': 'kanglong-wu', 'url': 'https://www.linkedin.com/in/kanglong-wu/'},
        'bilibili': {'user': 'wklchris', 'url': "https://space.bilibili.com/4595187"}
    },
    # 'people': people_json,
    # 'people_pages': ['People'],
    # 'photo_subpath': 'photos/'
}


# Others
templates_path = ['_templates']
rst_epilog = """
.. _Sphinx: https://www.sphinx-doc.org/
.. _sphinxcontrib-bibtex: https://sphinxcontrib-bibtex.readthedocs.io/
.. _recommonmark: https://recommonmark.readthedocs.io/en/latest/
"""