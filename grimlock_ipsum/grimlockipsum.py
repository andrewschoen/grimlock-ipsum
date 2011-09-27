import random

class GrimlockIpsumGenerator(object):
    def __init__(self, num_paragraphs=3, grimlock_case=False, 
            include_tweets=True, grimlock_tweet_caps=True, me_grimlock=False, 
            *args, **kwargs):
        super(GrimlockIpsumGenerator, self).__init__(*args, **kwargs)
        self.num_paragraphs = num_paragraphs
        self.grimlock_case = grimlock_case
        self.include_tweets = include_tweets
        self.grimlock_tweet_caps = grimlock_tweet_caps
        self.me_grimlock = me_grimlock
        
        self.grimlock_start_phrases = [
            'hurr hurr',
            'me, grimlock,',
            'me, grimlock, say',
            'me, grimlock, king!',
            'me like',
            'stupid,',
            'now time for #noeatfriday',
            '404 out of coffee error',
        ]

        self.grimlock_middle_phrases = [
            'hurr hurr',
            'coffee code code coffee code',
            'code code beer code beer',
            'bozo',
            'beryllium baloney',
            'cesium salami',
            'dinobots transform',
            'dinobots',
            'startup',
            'wrong',
            'boring',
            '#noeatfriday',
            'bacon',
            'transfomers',
            'stupid',
            'bacon, beer, boobs',
            'baconninjas',
            'baconkinis',
            'grimlocknauts',
            'girllocks',
            'beergineers',
            'baconinjas',
            'no like',
            'eaten',
            'me king',
            'beer',
            'boobs',
        ]

        self.grimlock_end_phrases = [
            'hurr hurr.',
            'or else!',
            'you will die!',
            'to kill!',
            'hooray!',
        ]

        self.grimlock_tweets = [
            'WHAT IS BEST IN LIFE? CRUSH THE CODE, DRIVE THE USERS BEFORE YOU, HEAR THE LAMENTATION OF THE ACCOUNTING DEPARTMENT.',
            'THE ENEMY OF MY ENEMY IS THE ONE I PUNCH SECOND.',
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
        ]

        self.ipsum_phrases = [
            'lorem ipsum dolor',
            'gusce dapibus ipsum eget',
            'turpis consectetur sed',
            'pellentesque placerat',
            'vivamus tempus',
            'dolor sit amet',
            'etiam blandit adipiscing',
            'adipiscing',
            'nunc aliquam leo',
            'semper elit',
            'sed vitae nisl',
            'sapien ut dignissim',
            'rutrum ipsum',
            'luctus',
            'donec a vulputate',
            'aenean, libero magna',
            'ante ut metus',
            'mauris at iaculis',
            'cras id bibendum nibh',
            'tellus felis, blandit aliquet',
            'nulla dui, euismod',
            'phasellus euismod sapien',
            'ut magna et urna',
            'hendrerit ultrices, libero tellus',
        ]

        self.ipsum_end_options = random.sample(self.ipsum_phrases, 5)
        self.ipsum_end_phrases = []
        for phrase in self.ipsum_end_options:
            self.ipsum_end_phrases.append(phrase + ".")

    def make_sentence(self, first_sentence=False):
        phrases = []
        num_phrases = random.choice([4,5,6,7])
        start_phrases = self.grimlock_start_phrases + self.ipsum_phrases
        middle_phrases = self.grimlock_middle_phrases + self.ipsum_phrases
        # trying to reduce the chance of getting all of one type in a sentence
        random.shuffle(middle_phrases)
        end_phrases = self.grimlock_end_phrases + self.ipsum_end_phrases
        for phrase in range(num_phrases):
            if phrase == 0:
                if first_sentence and self.me_grimlock:
                    phrase = "Me, Grimlock,"
                else:
                    phrase = random.choice(start_phrases)
                random.shuffle(start_phrases)
            elif phrase == num_phrases - 1:
                phrase = random.choice(end_phrases)
                random.shuffle(end_phrases)
            else:
                phrase = random.choice(middle_phrases)
                middle_phrases.remove(phrase)
                random.shuffle(middle_phrases)
            phrases.append(phrase)
        return " ".join(phrases).capitalize()
   
    def make_paragraph(self, first_paragraph=False):
        sentences = []
        num_sentences = random.choice([5,6,7,8,9])
        has_tweet = False
        for sentence in range(num_sentences):
            if first_paragraph and sentence == 0:
                sentences.append(self.make_sentence(first_sentence=True))
            else:
                sentences.append(self.make_sentence())
            if self.include_tweets and "y" in random.choice("nnyn") and not has_tweet:
                tweet = random.choice(self.grimlock_tweets)
                if not self.grimlock_tweet_caps:
                    # doesn't handle multiple sentences in the same string well
                    tweet = tweet.capitalize()
                sentences.append(tweet)
                self.grimlock_tweets.remove(tweet)
                has_tweet = True
        return " ".join(sentences)
        
    def generate(self):
        paragraphs = []
        for paragraph in range(self.num_paragraphs):
            first_paragraph = True if paragraph == 0 else False
            paragraphs.append("<p>")
            paragraphs.append(self.make_paragraph(first_paragraph=first_paragraph))
            paragraphs.append("</p>")
        if self.grimlock_case:
            return "".join(paragraphs).upper()
        return "".join(paragraphs)
    
    