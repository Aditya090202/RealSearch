import openai
import os
import re
from dotenv import load_dotenv


# def summarize_user_advice(question, user_responses):

def summarize_user_advice(user_messages):
    load_dotenv()
    openai.api_key = os.getenv('openai_api_key')
    # Construct the prompt
    system_message = 'Give a question summarize answers from users, making your response short, concise and maintaining key ideas and topics. Make sure to quote user. Example input Question: "What backend should I use", User: bob "I like django", User: george "Flask is very helpful".. Example Output "People recommend flask (@george) and django (@bob)"'
    # user_message = f"Question: \"{question}\"\n\n"
    # user_message += "\n".join([f"User:{user} \"{response}\"" for user, response in user_responses])

    # Make an API call to OpenAI
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_messages}
        ]
    )

    # Extract and return the summary from the API response
    return response['choices'][0]['message']['content']

def create_html_links(text):
    # Define a regular expression pattern to match usernames in the format (@username)
    pattern = r"\(@(\w+)\)"

    # Define a function that takes a match object and returns a string with the HTML link
    def replace_with_link(match):
        username = match.group(1)
        return f'<a href="/user/{username}">({username})</a>'

    # Use re.sub() to replace all occurrences of the pattern with the HTML link
    html_output = re.sub(pattern, replace_with_link, text)
    return html_output

# Example usage:
question = "Looking for advice on backend to choose"
user_responses = [
    ("Fox", "You're more likely to build something maintainable in a language and framework you are familiar with."),
    ("420", "If you are comfortable with Python, I would highly recommend the Django web framework. Flask is another popular Python web framework."),
    ("drdro", "If you have already decided on Vue i'd suggest to go for Node.")
]

