import django
import os
import pydoc

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "my_site.settings")
django.setup()

modules = [
    "supermercado.models",
    "supermercado.views",
]

for module in modules:
    pydoc.writedoc(module)