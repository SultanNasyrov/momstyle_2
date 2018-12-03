from .models import IconsPack

def icons(request):
    if IconsPack.objects.count() > 0:
        icons = IconsPack.objects.get()
    else:
        icons = {}
    return {'icons': icons}