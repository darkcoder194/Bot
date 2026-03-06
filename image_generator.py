from PIL import Image, ImageDraw, ImageFont

def create_image(topic):

    img = Image.new("RGB",(1080,1080),(30,30,30))

    draw = ImageDraw.Draw(img)

    font = ImageFont.load_default()

    draw.text((150,500), topic, fill="white", font=font)

    path = f"posts/{topic.replace(' ','_')}.png"

    img.save(path)

    return path