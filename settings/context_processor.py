from .models import IconsPack, Seo, SiteMain

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

def main(request):
    if SiteMain.objects.count() > 0:
        main = SiteMain.objects.get()
    else:
        main = {}
    return {'main': main}