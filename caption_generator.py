import random

templates = [

"🔥 Breaking anime news about {topic}!",
"{topic} is trending right now 👀",
"Anime fans are talking about {topic}",
"Otaku alert 🚨 {topic} is exploding online!",
"New anime update: {topic}"
]

def generate_caption(topic):

    text = random.choice(templates)

    return text.format(topic=topic)