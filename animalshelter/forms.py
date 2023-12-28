from django import forms
from .models import Animal,News,Review

class AnimalForm(forms.ModelForm):
    photo = forms.FileField(widget=forms.ClearableFileInput, required=False)  # Используем FileField для загрузки файла

    class Meta:
        model = Animal
        fields = '__all__'

class ReviewForm(forms.ModelForm):
    photo = forms.FileField(widget=forms.ClearableFileInput, required=False)  # Используем FileField для загрузки файла

    class Meta:
        model = Review
        fields = '__all__'

class AnimalFilterForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Заполните CHOICES значениями из базы данных
        self.fields['type_of_animal'] = forms.ChoiceField(
            choices=self.get_choices('type_of_animal'),
            required=False,
        )
        self.fields['sex'] = forms.ChoiceField(
            choices=self.get_choices('sex'),
            required=False,
        )
        self.fields['age'] = forms.ChoiceField(
            choices=self.get_choices('age'),
            required=False,
        )
        self.fields['size'] = forms.ChoiceField(
            choices=self.get_choices('size'),
            required=False,
        )
        self.fields['color'] = forms.ChoiceField(
            choices=self.get_choices('color'),
            required=False,
        )
        self.fields['temper'] = forms.ChoiceField(
            choices=self.get_choices('temper'),
            required=False,
        )

    def get_choices(self, field_name):
        values = Animal.objects.values_list(field_name, flat=True).distinct()
        return [('', 'Any')] + [(value, value.capitalize()) for value in values]
        
    def clear_filters(self):
        for field_name, _ in self.fields.items():
            self.cleaned_data[field_name] = ''
    # SEX_CHOICES=[
    #     ('','Any'),
    #     ('male','Male'),
    #     ('female','Female'),
    # ]
    # AGE_CHOICES = [
    #     ('', 'Any'),
    #     ('puppy', 'Puppy'),
    #     ('adult', 'Adult'),
    #     ('senior', 'Senior'),
    # ]

    # SIZE_CHOICES = [
    #     ('', 'Any'),
    #     ('small', 'Small'),
    #     ('medium', 'Medium'),
    #     ('large', 'Large'),
    # ]

    # COLOR_CHOICES = [
    #     ('', 'Any'),
    #     ('black', 'Black'),
    #     ('white', 'White'),
    #     ('brown', 'Brown'),
    #     # Добавьте свои цвета
    # ]

    # TEMPER_CHOICES = [
    #     ('', 'Any'),
    #     ('calm', 'Calm'),
    #     ('energetic', 'Energetic'),
    #     ('playful', 'Playful'),
    #     # Добавьте свои характеры
    # ]
    # sex=forms.ChoiceField(choices=SEX_CHOICES,required=False)
    # age = forms.ChoiceField(choices=AGE_CHOICES, required=False)
    # size = forms.ChoiceField(choices=SIZE_CHOICES, required=False)
    # color = forms.ChoiceField(choices=COLOR_CHOICES, required=False)
    # temper = forms.ChoiceField(choices=TEMPER_CHOICES, required=False)
 
class NewsForm(forms.ModelForm):
    photo = forms.FileField(widget=forms.ClearableFileInput, required=False)  # Используем FileField для загрузки файла

    class Meta:
        model = News
        fields = '__all__'

# class AddReview(forms.ModelForm):
#     class Meta(forms.ModelForm):
#         model = Review
#         fields = ("name", "description", "email")

#         widgets = {
#             "name": forms.TextInput(attrs={"class": "form-control"}),
#             "description": forms.TextInput(attrs={"class": "form-control"}),
#             "email": forms.TextInput(attrs={"class": "form-control"}),
#         }
