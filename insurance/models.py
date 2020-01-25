from django.db import models
from multiselectfield import MultiSelectField

class general_details(models.Model):
    fam_choices=(
    ('Diabetes','Diabetes'),
    ('Cancer','Cancer'),
    ('Eye Problem','Eye Problem'),
    ('Blood Pressure','Blood Pressure'),
    ('None','None'),
    )
    ab_choices=(
   ('Blind','Blind'),
   ('Deaf','Deaf'),
   ('Dyslexia','Dyslexia'),
   ('Physical deformation','Physical deformation'),
   ('Speech impairment','Speech impairment'),
    )
    income_choices=(
   ('Less than 5Lakh','Less than 5Lakh'),
   ('5 to 10Lakh','5 to 10Lakh'),
   ('More than 10Lakh','More than 10Lakh'),
    )
    name=models.CharField(max_length=100)
    age=models.IntegerField(max_length=10)
    height=models.IntegerField(max_length=10)
    weight=models.IntegerField(max_length=10)
    blood_group=models.CharField(max_length=10)
    vision=models.FloatField(max_length=10)
    gender= models.CharField(max_length=10)
    address=models.CharField(max_length=200)
    adhar_number=models.IntegerField(max_length=30)
    pan=models.CharField(max_length=100)
    abnormalities=MultiSelectField(choices=ab_choices)
    family_hist= MultiSelectField(choices=fam_choices)
    income=MultiSelectField(choices=income_choices)
    father_name=models.CharField(max_length=100)
    fathers_occ=models.CharField(max_length=100)
    mother_occ=models.CharField(max_length=100)
    mother_name=models.CharField(max_length=100)
    pob=models.CharField(max_length=100)
    dob=models.DateField()
    occupation=models.CharField(max_length=100)
    caste=models.CharField(max_length=100)
    phone_no=models.IntegerField(max_length=10)
    religious_minority= models.CharField(max_length=10)
    prev_insurance= models.CharField(max_length=10)
    nationality=models.CharField(max_length=100)
    image= models.ImageField(upload_to='media')
    sign= models.ImageField(upload_to='media')
    smoker = models.CharField(max_length=10)
    alcohol=models.CharField(max_length=10)


    def __str__(self):
        return self.name + ' - ' + self.father_name
class vital(models.Model):
    vitals = models.ForeignKey(general_details, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    sugar= models.FloatField(max_length=10)
    mcv= models.FloatField(max_length=10)
    haemoglobin = models.FloatField(max_length=10)
    cholestrol= models.FloatField(max_length=10)
    bp= models.FloatField(max_length=10)
    pulse_rate= models.FloatField(max_length=10)
    total_rbc= models.FloatField(max_length=10)
    pcv= models.FloatField(max_length=10)
    platelet_count= models.FloatField(max_length=10)
    leucocytes_count= models.FloatField(max_length=10)
    tsh= models.FloatField(max_length=10)
    glucose_content= models.FloatField(max_length=10)
    bilirubin= models.FloatField(max_length=10)
    ph= models.FloatField(max_length=10)
    wbc_count=models.FloatField(max_length=10)


class chronic(models.Model):
    chronics = models.ForeignKey(general_details, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    ckd_test=models.FloatField(max_length=10)
    egfr=models.FloatField(max_length=10)
    creatinine=models.FloatField(max_length=10)
    uric_acid=models.FloatField(max_length=10)
    Urea=models.FloatField(max_length=10)
    ecg=models.FloatField(max_length=10)
    emg_test=models.FloatField(max_length=10)

class accident_insurance(models.Model):
    accident_insurance = models.ForeignKey(general_details, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    x_ray=models.CharField(max_length=100)
    ct_scan=models.CharField(max_length=100)
    mri=models.CharField(max_length=100)
    others=models.CharField(max_length=100)

class chronic_month2(models.Model):
    chronics = models.ForeignKey(general_details, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    ckd_test=models.FloatField(max_length=10)
    egfr=models.FloatField(max_length=10)
    creatinine=models.FloatField(max_length=10)
    uric_acid=models.FloatField(max_length=10)
    Urea=models.FloatField(max_length=10)
    ecg=models.FloatField(max_length=10)
    emg_test=models.FloatField(max_length=10)


class chronic_month3(models.Model):
    chronics = models.ForeignKey(general_details, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    ckd_test=models.FloatField(max_length=10)
    egfr=models.FloatField(max_length=10)
    creatinine=models.FloatField(max_length=10)
    uric_acid=models.FloatField(max_length=10)
    Urea=models.FloatField(max_length=10)
    ecg=models.FloatField(max_length=10)
    emg_test=models.FloatField(max_length=10)


class vital2(models.Model):
    vitals = models.ForeignKey(general_details, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    sugar= models.FloatField(max_length=10)
    mcv= models.FloatField(max_length=10)
    haemoglobin = models.FloatField(max_length=10)
    cholestrol= models.FloatField(max_length=10)
    bp= models.FloatField(max_length=10)
    pulse_rate= models.FloatField(max_length=10)
    total_rbc= models.FloatField(max_length=10)
    pcv= models.FloatField(max_length=10)
    platelet_count= models.FloatField(max_length=10)
    leucocytes_count= models.FloatField(max_length=10)
    tsh= models.FloatField(max_length=10)
    glucose_content= models.FloatField(max_length=10)
    bilirubin= models.FloatField(max_length=10)
    ph= models.FloatField(max_length=10)
    wbc_count=models.FloatField(max_length=10)


class vital3(models.Model):
    vitals = models.ForeignKey(general_details, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    sugar= models.FloatField(max_length=10)
    mcv= models.FloatField(max_length=10)
    haemoglobin = models.FloatField(max_length=10)
    cholestrol= models.FloatField(max_length=10)
    bp= models.FloatField(max_length=10)
    pulse_rate= models.FloatField(max_length=10)
    total_rbc= models.FloatField(max_length=10)
    pcv= models.FloatField(max_length=10)
    platelet_count= models.FloatField(max_length=10)
    leucocytes_count= models.FloatField(max_length=10)
    tsh= models.FloatField(max_length=10)
    glucose_content= models.FloatField(max_length=10)
    bilirubin= models.FloatField(max_length=10)
    ph= models.FloatField(max_length=10)
    wbc_count=models.FloatField(max_length=10)


class registration(models.Model):
    first_name=models.CharField(max_length=100)
    last_name= models.CharField(max_length=100)
    phone=models.IntegerField(max_length=10)
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)

class ocr(models.Model):
    ocr = models.ForeignKey(general_details, on_delete=models.CASCADE)
    img= models.ImageField(upload_to='media/')
