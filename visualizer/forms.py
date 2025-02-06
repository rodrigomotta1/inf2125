from django import forms
from visualizer.models import UserProfile, Place

class UserSettingsForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['notifications_enabled']
        widgets = {
            'notifications_enabled': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }

class InformationUploadForm(forms.Form):
    INFO_TYPES = (
        ("third_party", "Fonte Oficial"),
        ("video", "Vídeo"),
        ("image", "Imagem"),
    )

    place = forms.ModelChoiceField(
        queryset=Place.objects.all(),
        label="Local",
        widget=forms.Select(attrs={'class': 'form-select'}),
        empty_label="Selecione um local",
    )

    info_type = forms.ChoiceField(choices=INFO_TYPES, label="Tipo de Informação", widget=forms.Select(attrs={'class': 'form-select'}))
    title = forms.CharField(label="Título", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(label="Descrição", widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}))
    source_name = forms.CharField(required=False, label="Fonte", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    source_url = forms.URLField(required=False, label="URL da Fonte", widget=forms.URLInput(attrs={'class': 'form-control'}))
    video_url = forms.URLField(required=False, label="URL do Vídeo", widget=forms.URLInput(attrs={'class': 'form-control'}))
    image = forms.ImageField(required=False, label="Imagem", widget=forms.FileInput(attrs={'class': 'form-control'}))