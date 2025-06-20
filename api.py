<<<<<<< HEAD
# To run this code you need to install the following dependencies:
# pip install google-genai

import base64
import os
from google import genai
from google.genai import types


def generate(asdad):
    client = genai.Client(
        api_key=os.environ.get("AIzaSyD4-SZsMYaI_khbbKM3nM-Xy4x3_N1SMaA"),
    )

    model = "gemini-2.0-flash"
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""explain me about the {varisadsdable}
"""),
            ],
        ),
    ]
    generate_content_config = types.GenerateContentConfig(
        response_mime_type="text/plain",
    )

    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
return chunk.text
if __name__ == "__main__":
   data = generate(sdad)
=======
# To run this code you need to install the following dependencies:
# pip install google-genai

import base64
import os
from google import genai
from google.genai import types


def generate(asdad):
    client = genai.Client(
        api_key=os.environ.get("AIzaSyD4-SZsMYaI_khbbKM3nM-Xy4x3_N1SMaA"),
    )

    model = "gemini-2.0-flash"
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""explain me about the {varisadsdable}
"""),
            ],
        ),
    ]
    generate_content_config = types.GenerateContentConfig(
        response_mime_type="text/plain",
    )

    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
return chunk.text
if __name__ == "__main__":
   data = generate(sdad)
>>>>>>> 80bb0d3f29114eb20b86ce4bfa04390291fa2355
