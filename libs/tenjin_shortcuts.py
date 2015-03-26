import tenjin
from django.conf import settings
from tenjin.helpers import *

engine = tenjin.Engine(path= settings.TEMPLATE_DIRS, cache=tenjin.MemoryCacheStorage(), preprocess=True)

def render_to_response(template, context=None, context_instance=None, globals=None, layout=False):
    if context is None:
        context = {}
    context.update({
        'request': context_instance,
    })
    try:
        CDN_URL = settings.CDN_URL
        context.update({
            'CDN_URL': CDN_URL,
        })
    except:
        pass
    return engine.render(template, context, globals, layout)
