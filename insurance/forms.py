from django import forms


from .models import general_details,ocr



class general_details_form(forms.ModelForm):

    class Meta:
        model = general_details
        fields = ['name',
        'age',
        'height',
        'weight',
        'blood_group',
        'vision',
        'gender',
        'address',
        'adhar_number',
        'pan',
        'abnormalities',
        'family_hist',
        'income',
        'father_name',
        'fathers_occ',
        'mother_occ',
        'mother_name',
        'pob',
        'dob',
        'occupation',
        'caste',
        'phone_no',
        'religious_minority',
        'prev_insurance',
        'nationality',
        'image',
        'sign',
        'smoker',
        'alcohol']


class uploadform(forms.ModelForm):

    class Meta:
        model = general_details
        fields = ['image','sign']

class uploadocr(forms.ModelForm) :
    class Meta:
        model = ocr
        fields = ['img']
