from django.views.generic import TemplateView

class IndexView(TemplateView):
    """Class-based view for index page."""

    template_name = "index.html"
