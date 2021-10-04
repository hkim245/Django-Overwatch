import datetime

from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class RenewBookForm(forms.Form):
    renewal_date = forms.DateField(help_text="Enter a date between now and 4 weeks (default 3).")

    def clean_renewal_date(self):
        data = self.cleaned_data['renewal_date']
        
        # Check if a date is not in the past. 
        if data < datetime.date.today():
            raise ValidationError(_('Invalid date - renewal in past'))

        # Check if a date is in the allowed range (+4 weeks from today).
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(_('Invalid date - renewal more than 4 weeks ahead'))

        # Remember to always return the cleaned data.
        return data	
		
class createTeamList(forms.Form):
    name = forms.CharField(label = "Enter a name for your team composition", max_length=100)
		

	
class CreateNewList(forms.Form):
    name = forms.CharField(label="Name", max_length=200)
    check = forms.BooleanField(required=False)
	
class createTeamComposition(forms.Form):
    BattleTag_1 = forms.CharField(label = "BattleTag 1", max_length=100)
    BattleTag_2 = forms.CharField(label = "BattleTag 2", max_length=100)
    BattleTag_3 = forms.CharField(label = "BattleTag 3", max_length=100)
    BattleTag_4 = forms.CharField(label = "BattleTag 4", max_length=100)
    BattleTag_5 = forms.CharField(label = "BattleTag 5", max_length=100)
    BattleTag_6 = forms.CharField(label = "BattleTag 6", max_length=100)
    '''Hero_1 = forms.CharField(label = "Hero 1", max_length=50)
    Hero_2 = forms.CharField(label = "Hero 2", max_length=50)
    Hero_3 = forms.CharField(label = "Hero 3", max_length=50)
    Hero_4 = forms.CharField(label = "Hero 4", max_length=50)
    Hero_5 = forms.CharField(label = "Hero 5", max_length=50)
    Hero_6 = forms.CharField(label = "Hero 6", max_length=50)'''	
	
class createTeamComposition2(forms.Form):
    BattleTag_1 = forms.CharField(label = "BattleTag 1", max_length=100)
    BattleTag_2 = forms.CharField(label = "BattleTag 2", max_length=100)
	
class createTeamComposition3(forms.Form):
    BattleTag_1 = forms.CharField(label = "BattleTag 1", max_length=100)
    BattleTag_2 = forms.CharField(label = "BattleTag 2", max_length=100)
    BattleTag_3 = forms.CharField(label = "BattleTag 3", max_length=100)
	
class createTeamComposition4(forms.Form):
    BattleTag_1 = forms.CharField(label = "BattleTag 1", max_length=100)
    BattleTag_2 = forms.CharField(label = "BattleTag 2", max_length=100)
    BattleTag_3 = forms.CharField(label = "BattleTag 3", max_length=100)
    BattleTag_4 = forms.CharField(label = "BattleTag 4", max_length=100)
	
class createTeamComposition5(forms.Form):
    BattleTag_1 = forms.CharField(label = "BattleTag 1", max_length=100)
    BattleTag_2 = forms.CharField(label = "BattleTag 2", max_length=100)
    BattleTag_3 = forms.CharField(label = "BattleTag 3", max_length=100)
    BattleTag_4 = forms.CharField(label = "BattleTag 4", max_length=100)
    BattleTag_5 = forms.CharField(label = "BattleTag 5", max_length=100)
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	