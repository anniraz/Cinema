from modeltranslation.translator import  TranslationOptions,register
from .models import *

@register(Movie)
class ModelkaTranslationOptions(TranslationOptions):
    
    fields = ('name', 'description','country')
    
@register(News)
class NewsTranslation(TranslationOptions):
    fields=('title','description')