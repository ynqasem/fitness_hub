from django.core.urlresolvers import reverse
from django import forms
from django.core.validators import RegexValidator
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.layout import HTML, Layout, Div, Field
from crispy_forms.bootstrap import FormActions

from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from django import forms

from app.models import CustomUser, Image, Gym

class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        #del self.fields['username']

    class Meta:
        model = CustomUser
        fields = ("first_name","last_name","number","email","password1", "password2")

    def __init__(self, *args, **kwargs):
            super(CustomUserCreationForm, self).__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.form_method = 'post'
            self.helper.form_action ='/signup/'
            self.helper.layout= Layout(
                Div(
                        Div('first_name',css_class='col-sm-4',),
                        css_class='row'
                    ),
                Div(
                        Div('last_name',css_class='col-sm-4',),
                        css_class='row'
                    ),
                Div(
                        Div('number',css_class='col-sm-4',),
                        css_class='row'
                    ),      
                Div(
                        Div('email',css_class='col-sm-4',),
                        css_class='row'
                    ),
                
                Div(
                        Div('password1',css_class='col-sm-4',),
                        css_class='row'
                    ),
                Div(
                        Div('password2',css_class='col-sm-4',), 
                        css_class='row'
                    ),
                Div(
                        Div(FormActions(Submit('submit','Sign Up')), css_class='col-sm-12'),
                        css_class='row'
                    )
                )

class CustomUserChangeForm(UserChangeForm):
    def __init__(self, *args, **kwargs):
        super(CustomUserChangeForm, self).__init__(*args, **kwargs)
        #del self.fields['username']

    class Meta:
        model = CustomUser
        fields = '__all__'



class CustomUserLoginForm(forms.Form):
    email = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
            super(CustomUserLoginForm, self).__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.form_method = 'post'
            self.helper.form_action ='/login/'
            self.helper.layout= Layout(
                Div(
                        Div('email',css_class='col-sm-4',type="hidden"),
                        css_class='row'
                    ),
                Div(
                        Div('password',css_class='col-sm-4',),
                        css_class='row'
                    ),
                Div(
                        Div(FormActions(Submit('submit','Login')), css_class='col-sm-12'),
                        css_class='row'
                    )
                )

# class CreateGym(forms.ModelForm):
#     # images = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
#     class Meta:
#         model = Gym

#         fields = '__all__'

#     def __init__(self, *args, **kwargs):
#             super(CreateGym, self).__init__(*args, **kwargs)
#             self.helper = FormHelper()
#             self.helper.form_method = 'post'
#             self.helper.form_action ='/create_gym/'
#             self.helper.form_id = 'cform'
#             self.helper.layout= Layout(
#                         Div(    Div('gym_name',css_class='col-sm-6',), 
#                                 css_class='row'
#                             ),
#                         Div(    Div('description',css_class='col-sm-6',), 
#                                 css_class='row'
#                             ),
#                         Div(    Div('location',css_class='col-sm-6',), 
#                                 css_class='row'
#                             ),
#                         Div(    Div('gender',css_class='col-sm-6',), 
#                                 css_class='row'
#                             ),
#                         Div(    Div('number',css_class='col-sm-6',), 
#                                 css_class='row'
#                             ),
#                         Div(    Div('logo',css_class='col-sm-6',), 
#                                 css_class='row'
#                             ),
#                         # Div(    Div('images',css_class='col-sm-6',), 
#                         #         css_class='row'
#                         #     ),
#                         Div(FormActions(Submit('submit','Save')), css_class='col-sm-12')
#                         )

class CreateGym(forms.ModelForm):
    class Meta:
        model = Gym

        fields = '__all__'
    def __init__(self, *args, **kwargs):
            super(CreateGym, self).__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.form_method = 'post'
            self.helper.form_action ='/create_gym/'
            #self.helper.add_input(Submit('submit', 'Search'))
            self.helper.layout= Layout(
                Div(    Div('gym_name',css_class='col-sm-6',), 
                                css_class='row'
                            ),
                Div(    Div('description',css_class='col-sm-6',), 
                                css_class='row'
                            ),
                Div(    Div('location',css_class='col-sm-6',), 
                                css_class='row'
                            ),
                Div(    Div('gender',css_class='col-sm-6',), 
                                css_class='row'
                            ),
                Div(    Div('number',css_class='col-sm-6',), 
                                css_class='row'
                            ),
                Div(    Div('logo',css_class='col-sm-6',), 
                                css_class='row'
                            ),
                Div(    Div('lati',css_class='col-sm-6',), 
                                css_class='row'
                            ),
                Div(    Div('longi',css_class='col-sm-6',), 
                                css_class='row'
                            ),
                Div(    Div('file1',css_class='col-sm-6',), 
                                css_class='row'
                            ),
                Div(    Div('file2',css_class='col-sm-6',), 
                                css_class='row'
                            ),
                Div(    Div('file3',css_class='col-sm-6',), 
                                css_class='row'
                            ),
                Div(    Div('file4',css_class='col-sm-6',), 
                                css_class='row'
                            ),
                Div(    Div('file5',css_class='col-sm-6',), 
                                css_class='row'
                            ),
                Div(FormActions(Submit('submit','Save')), css_class='col-sm-12')
                        )

class EditGym(forms.ModelForm):
    class Meta:
        model = Gym

        fields = '__all__'
    def __init__(self, *args, **kwargs):
            super(EditGym, self).__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.form_method = 'post'
            self.helper.form_action = reverse('edit_gym', kwargs={'pk':self.instance.pk})
            self.helper.layout= Layout(
                Div(    Div('gym_name',css_class='col-sm-6',), 
                                css_class='row'
                            ),
                Div(    Div('description',css_class='col-sm-6',), 
                                css_class='row'
                            ),
                Div(    Div('location',css_class='col-sm-6',), 
                                css_class='row'
                            ),
                Div(    Div('gender',css_class='col-sm-6',), 
                                css_class='row'
                            ),
                Div(    Div('number',css_class='col-sm-6',), 
                                css_class='row'
                            ),
                Div(    Div('logo',css_class='col-sm-6',), 
                                css_class='row'
                            ),
                Div(    Div('lati',css_class='col-sm-6',), 
                                css_class='row'
                            ),
                Div(    Div('longi',css_class='col-sm-6',), 
                                css_class='row'
                            ),
                Div(    Div('file1',css_class='col-sm-6',), 
                                css_class='row'
                            ),
                Div(    Div('file2',css_class='col-sm-6',), 
                                css_class='row'
                            ),
                Div(    Div('file3',css_class='col-sm-6',), 
                                css_class='row'
                            ),
                Div(    Div('file4',css_class='col-sm-6',), 
                                css_class='row'
                            ),
                Div(    Div('file5',css_class='col-sm-6',), 
                                css_class='row'
                            ),
                Div(FormActions(Submit('submit','Save')), css_class='col-sm-12')
                        )