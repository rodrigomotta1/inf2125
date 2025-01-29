from django.contrib import admin

from .models import Place, Estimate, ImageInformation, VideoInformation, ThirdPartyInformation, UserProfile

admin.site.register(Place)
admin.site.register(Estimate)
admin.site.register(ImageInformation)
admin.site.register(VideoInformation)
admin.site.register(ThirdPartyInformation)
admin.site.register(UserProfile)