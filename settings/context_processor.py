from .models import IconsPack,Seo

def icons(request):
    if IconsPack.objects.count() > 0:
        icons = IconsPack.objects.get()
    else:
        icons = {}
    return {'icons': icons}

def seo(request):
    if Seo.objects.count() > 0:
        seo = Seo.objects.get()
    else:
        seo = {}
    return {'seo': seo}