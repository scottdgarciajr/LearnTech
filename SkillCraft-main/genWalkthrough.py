import openai

# Set your OpenAI API key
openai.api_key = "INSERT_API_KEY_HERE"




def generate_project_ideas(skill, level):
    prompt = f"Generate 10 project ideas that involve {skill} at a {level} level."
    response = openai.Completion.create(
        engine="davinci-codex",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )
    ideas = response.choices[0].text.strip().split("\n")
    return ideas

def generate_project_description(idea):
    prompt = f"Generate a project description for a {idea} at a beginner/intermediate/expert level."
    response = openai.Completion.create(
        engine="davinci-codex",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )
    description = response.choices[0].text.strip()
    return description

def generate_steps(project, description):
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




def generate_walkthroughs(project, description, steps):
    # Create an empty string to store the walkthroughs
    walkthroughs = ""

    # Generate a walkthrough for each step
    for step in steps:
        # Generate the walkthrough for the current step
        walkthrough = generate_walkthrough(project, description, step)

        # Add the walkthrough to the string
        walkthroughs += f"Step: {step}\n{walkthrough}\n\n"

    # Return the string of walkthroughs
    return walkthroughs







