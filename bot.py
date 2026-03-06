import schedule
import time

from news_scraper import get_all_news
from trending_anime import get_trending
from caption_generator import generate_caption
from image_generator import create_image
from hashtag_generator import generate
from instagram_poster import post
from database import is_posted, save_post


def run_bot():

    news = get_all_news()

    if not news:
        topic = get_trending()
    else:
        topic = news[0]

    if is_posted(topic):
        print("Already posted:", topic)
        return

    caption = generate_caption(topic)

    hashtags = generate()

    image = create_image(topic)

    final_caption = f"{caption}\n\n{hashtags}"

    post(image, final_caption)

    save_post(topic)

    print("Posted:", topic)


schedule.every(4).hours.do(run_bot)

while True:

    schedule.run_pending()

    time.sleep(60)