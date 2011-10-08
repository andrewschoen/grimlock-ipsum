import random

from django.views.generic import FormView, TemplateView
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from forms import GrimlockIpsumForm
from grimlockipsum import GrimlockIpsumGenerator

grimlock_tweets = [
    'WHAT IS BEST IN LIFE? CRUSH THE CODE, DRIVE THE USERS BEFORE YOU, HEAR THE LAMENTATION OF THE ACCOUNTING DEPARTMENT.',
    'LOOK LIKE SOMEONE NEED PUNCH IN FACE. THAT SOMEONE IS EVERYONE.',
    'ONLY WAY YOU GETTING OUT OF HERE ALIVE IS DEAD.',
    'ME, GRIMLOCK, HERE TO WRITE CODE AND DRINK COFFEE. UNLESS US OUT OF COFFEE. THEN ME HERE TO KILL EVERYONE.',
    'THERE WILL BE COFFEE. OR DEATH. MAKE CHOICE.',
    'BEST THINGS IN LIFE ARE FREE. LIKE PUNCH YOU IN FACE. SEE? IT NOT COST ME ANYTHING.',
    'ME HAVE FORMAT AND REINSTALL READY FOR YOU. IT LOADED IN FIST.',
    'GREEDY IS SUBSET OF STUPID.',
    'HOW MORNING HAPPEN AGAIN? STUPID WORLD.',
    'WHAT TASTE BETTER WITH BACON? EVERYTHING.',
    '//OUT OF COFFEE ERROR. INSERT ADDITIONAL COFFEE TO CONTINUE, OR EVERYONE WILL DIE. EVERY. ONE.',
    'SOMEONE NEED TO RECODE MONDAY. RESPAWN RATE TOO HIGH, AND NEVER DROP GOOD LOOT.',
    'MOST BUGS RESULT OF HUMAN ERROR. ONLY WAY TO FIX THIS IS REMOVE ALL HUMANS.',
    'ME, GRIMLOCK, SAY "LET THERE BE BEER." AND THERE AM BEER. OR ELSE.',
    'TIME TO CLOSE OFFICE FOR NIGHT. WITH FIRE.',
    'ME ONLY HAVE ONE ADVICE: BE AWESOME. EVERYTHING ELSE DETAILS.',
    'ME KINDA LIKE CHUCK NORRIS BUT NOT GET OLD AND SMELLY.  ALSO ME NOT HAVE WEIRD FACIAL HAIR.',
]

class HomeView(FormView):
    template_name = "home.html"
    form_class = GrimlockIpsumForm
    success_url = '/words/'
    
    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        intro_tweet = random.choice(grimlock_tweets)
        context.update({
            "intro_tweet":intro_tweet
        })
        return context
        
class GrimlockIpsumView(TemplateView):
    template_name = "ipsum.html"
    
    def get_context_data(self, **kwargs):
        context = super(GrimlockIpsumView, self).get_context_data(**kwargs)
        request = self.request
        paragraphs = request.GET.get("paragraphs", 3)
        case = request.GET.get("type", "quiet")
        grimlock_case = True if "loud" in case.lower() else False
        me_grimlock = request.GET.get("me_grimlock", False)
        include_tweets = request.GET.get("tweets", False)
        generator = GrimlockIpsumGenerator(num_paragraphs=int(paragraphs),
                            grimlock_case=grimlock_case, me_grimlock=me_grimlock,
                            include_tweets=include_tweets)
        grimlock_ipsum = generator.generate()
        context.update({
            "grimlock_ipsum":grimlock_ipsum,
            'form':GrimlockIpsumForm()
        })
        return context