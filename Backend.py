from flask import Flask, render_template, request
import openai

app = Flask(__name__)

# Configure OpenAI API
openai.api_key = 'YOUR_API_KEY'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    topic = request.form['topic']
    skill_level = request.form['skill_level']

    # Make a request to the OpenAI API
    response = openai.Completion.create(
        engine='davinci-3',
        prompt=f"I want to create a project on {topic} and my skill level is {skill_level}.",
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.7
    )

    project_ideas = response.choices[0].text.strip()

    return render_template('result.html', project_ideas=project_ideas)

if __name__ == '__main__':
    app.run(debug=True)
