from django.forms import ModelForm,widgets,modelformset_factory
from django import forms
from .models import List,Task

class ListForm(ModelForm):
    class Meta:
        model = List
        fields = ['title']
        labels = {'title':''}

    def __init__(self, *args, **kwargs):
        super(ListForm,self).__init__(*args, **kwargs)

        for name,field in self.fields.items():
                field.widget.attrs.update({'onChange':'submit();',
                                            'style':'border:none;max-width:200px;',
                                            'class':'bg-light',
                                            'placeholder':'Enter list name...',})


#To  use widgets use exactly "from django import forms"
TaskFormSet = modelformset_factory(
    Task, fields=('completed','name'),
    labels={'completed':'completed','name':'name'},
    widgets={
        'completed': forms.CheckboxInput(attrs={
                'onChange':'submit();',
                'class':'faChkRnd',
                }),
        'name':forms.Textarea(attrs={
                'onChange':'submit();',
                # 'oninput':'this.style.height = "";this.style.height = this.scrollHeight + 3+"px"',
                'rows':'2',
                'class':'get-striked',
                'placeholder':'+ Add new task...'
                })          
    },
    )
     
class ShareForm(forms.Form):
    coowner = forms.CharField(label='', max_length=100)

    def __init__(self, *args, **kwargs):
        super(ShareForm,self).__init__(*args, **kwargs)

        for name,field in self.fields.items():
                field.widget.attrs.update({ 'class':'form-control',
                                            'placeholder':'Enter username or email of ListMaker...'})