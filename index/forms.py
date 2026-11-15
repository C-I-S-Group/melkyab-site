from index.models import Conntact
from django.forms import ModelForm


class FormConntact(ModelForm):
    class Meta:
        model = Conntact
        fields = "__all__"
