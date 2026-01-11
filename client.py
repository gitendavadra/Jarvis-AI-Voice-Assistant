# Import the OpenAI client library
from openai import OpenAI
# Create a single OpenAI client using your API key So this client will be reused for every AI request
client = OpenAI(api_key="YOUR_API_KEY")

def ask_jarvis(prompt):
    """
    This function sends the user's command to OpenAI
    and returns Jarvis's intelligent reply.
    """
    # Send the user input to the OpenAI model
    response = client.responses.create(
        model="gpt-4o-mini",   # Fast and cost-efficient AI model
        input=[
            {
                "role": "system",
                "content": "You are a virtual assistant named Jarvis skilled in general tasks like Alexa and Google Cloud. Give short responses."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    return response.output_text    # Extract and return the text response from the AI