from django.views.generic import FormView, TemplateView
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from forms import GrimlockIpsumForm
from grimlockipsum import GrimlockIpsumGenerator

class HomeView(FormView):
    template_name = "home.html"
    form_class = GrimlockIpsumForm
    success_url = '/words/'
        
class GrimlockIpsumView(TemplateView):
    template_name = "ipsum.html"
    
    def get_context_data(self, **kwargs):
        context = super(GrimlockIpsumView, self).get_context_data(**kwargs)
        request = self.request
        paragraphs = request.GET.get("paragraphs", 3)
        case = request.GET.get("type", "quiet")
        grimlock_case = True if "loud" in case.lower() else False
        generator = GrimlockIpsumGenerator()
        grimlock_ipsum = generator.generate(num_paragraphs=int(paragraphs), 
                            grimlock_case=grimlock_case)
        context.update({
            "grimlock_ipsum":grimlock_ipsum,
        })
        return context
    