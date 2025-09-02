import base64
from io import BytesIO
from openai import OpenAI
from PIL import Image
from dotenv import load_dotenv

load_dotenv(override=True)
openai = OpenAI()


def artist(city):
    """Generate an image for a destination city using DALL-E 3"""
    image_response = openai.images.generate(
        model="dall-e-3",
        prompt=f"An image representing a vacation in {city}, showing tourist spots and everything unique about {city}, in a vibrant pop-art style",
        size="1024x1024",
        n=1,
        response_format="b64_json",
    )
    image_base64 = image_response.data[0].b64_json
    image_data = base64.b64decode(image_base64)
    return Image.open(BytesIO(image_data))


def generate_image_async(history):
    """Generate image asynchronously after text response"""
    if not history:
        return None

    # Check if the last message was about a destination city
    for msg in reversed(history):
        if msg.get("role") == "tool":
            try:
                import json
                tool_data = json.loads(msg.get("content", "{}"))
                city = tool_data.get("destination_city")
                if city:
                    return artist(city)
            except:
                pass

    return None
