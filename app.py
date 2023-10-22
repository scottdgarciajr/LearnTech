
from flask import Flask, render_template, request
import openai
import json

app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    # Configure OpenAI API
    openai.api_key = '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'
    topic = request.form['topic']
    skill_level = request.form['skill_level']

    # Make a request to the OpenAI API
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5,
    )

    project_ideas = response.choices[0].text.strip()

    return render_template('result.html', project_ideas=project_ideas)

@app.route('/generate_project_ideas', methods=['POST'])
def generate_project_ideas():
    # Configure OpenAI API
    openai.api_key = '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'
    # Parse the JSON payload
    data = json.loads(request.data)
    skill = data['skill']
    level = data['level']

    # Generate project ideas using OpenAI's GPT-3 API
    ideas = generate_project_ideas(skill, level)

    # Return the project ideas as a JSON response
    return json.dumps(ideas)

def generate_project_ideas(skill, level):
    # Configure OpenAI API
    openai.api_key = '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'
    prompt = f"Generate 10 project ideas that involve {skill} at a {level} level."
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )
    ideas = response.choices[0].text.strip().split("\n")
    return ideas


@app.route('/generate_project_description', methods=['POST'])
def generate_project_description(idea):
    # Configure OpenAI API
    openai.api_key = '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'
    prompt = f"Generate a project description for a {idea}."
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )
    description = response.choices[0].text.strip()
    return description

@app.route('/generate_steps', methods=['POST'])
def generate_steps(project, description):
    # Configure OpenAI API
    openai.api_key = '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'
    # Define the prompt for the current project idea and description
    prompt = f"Generate a list of steps to complete the project '{project}' and {description} and save it to an array."
    
    # Generate text using OpenAI's Completion module
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Create an empty list to store the steps
    steps = []

    # Append each output to the list of steps
    for choice in response.choices:
        steps.append(choice.text)

    # Return the list of steps
    return steps




import openai


def generate_walkthrough(project, description, step):
    # Define the prompt for the current step
    # Configure OpenAI API
    openai.api_key = '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'
    prompt = f"Provide a walkthrough of how to complete the step '{step}' for the project '{project}' and {description}."
    
    # Generate text using OpenAI's Completion module
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1000,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Extract the walkthrough from the response
    walkthrough = response.choices[0].text.strip()

    # Return the walkthrough
    return walkthrough



@app.route('/generate_walkthroughs', methods=['POST'])
def generate_walkthroughs():
    # Configure OpenAI API
    openai.api_key = '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'
    # Parse the JSON payload
    data = json.loads(request.data)
    project = data['project']

    # Generate project ideas using OpenAI's GPT-3 API
    ideas = generate_walkthroughs(project)

    # Return the project ideas as a JSON response
    return json.dumps(ideas)


def generate_walkthroughs(project):
    description = generate_project_description(project)
    # Create an empty list to store the walkthroughs
    walkthroughs = []
    steps = generate_steps(project, description)

    # Generate a walkthrough for each step
    for step in steps:
        # Generate the walkthrough for the current step
        walkthrough = generate_walkthrough(project, description, step)

        # Create a new list for the current walkthrough
        current_walkthrough = walkthrough

        # Append the new list to the main list of walkthroughs
        walkthroughs.append(current_walkthrough)


    # Return the list of walkthroughs
    return walkthroughs





if __name__ == '__main__':
    app.run(debug=True)
