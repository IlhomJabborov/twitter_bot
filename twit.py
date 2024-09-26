from ntscraper import Nitter


class TwitterPost():
    def __init__(self) -> None:
        self.scraper = Nitter()
        
    def twit_post(self):
        tweets = self.scraper.get_tweets("FCBarcelona", mode="user", number=2)
        
        if tweets:
            final_tweets = []
            for x in tweets['tweets']:
                data = [x['link'], x['text'], x['pictures'], x['videos'], x['gifs']]
                final_tweets.append(data)

            return final_tweets[1]
