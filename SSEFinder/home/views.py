from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "home.html"


class ViewCase(TemplateView):
    template_name = "viewCase.html"


class ViewSSE(TemplateView):
    template_name = "viewSSE.html"
