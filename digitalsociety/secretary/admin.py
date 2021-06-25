from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(User)
admin.site.register(Chairman)
admin.site.register(Members)
admin.site.register(Myfamily)
admin.site.register(EditMyfamily)
admin.site.register(NoticeBoard)
admin.site.register(Events)
admin.site.register(Complain)
admin.site.register(Suggestions)
admin.site.register(Vistiors)

