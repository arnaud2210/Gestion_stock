from django import forms
from .models import Article
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field
from crispy_forms.bootstrap import  FormActions


class ArticleForm(forms.Form):
    
    code = forms.CharField(max_length=5, label='Code produit')
    label = forms.CharField(max_length=200, label='Libellé')
    price = forms.FloatField(label='Prix')
    quantity = forms.IntegerField(label='Quantité')
    creation = forms.DateField(label='Date de création')



    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.layout = Layout(

        Field('code', css_class='input-xlarge'),
        Field('label', css_class='input-xlarge'),
        Field('price', css_class='input-xlarge'),
        Field('quantity', css_class='input-xlarge'),
        Field('creation', css_class='input-xlarge'),

        FormActions(
            Submit('save_changes', 'ajouter', css_class="btn-secondary"),
        )
)