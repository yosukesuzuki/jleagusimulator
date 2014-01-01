from kay.utils import forms
from kay.utils.forms.modelform import ModelForm
from mainapp.models import AdminPage,Article,JPlayerData

class AdminPageForm(ModelForm):
    class Meta:
         model = AdminPage 
         exclude = ('images','lang','page_order','update','created')

class ArticleForm(ModelForm):
    class Meta:
         model = Article
         exclude = ('images','lang','page_order','update','created','tags')

class JPlayerDataForm(ModelForm):
    class Meta:
         model = JPlayerData 
#         exclude = ()

