# main.py
# -----------------------------------------------------------------
# Additional configuration/processing for GCSE CS site
# =================================================================
import json
import re
from markdown import markdown

def define_env(env):

    @env.macro
    def get_message(n):
        return f"??? Hello\n\t{n}"

    def render_quiz(quiz_data):
        def apply_code_tags(text):
        # This function finds text enclosed in backticks and wraps it with <code> tags
            return re.sub(r'`([^`]*)`', r'<code>\1</code>', text)

        quiz_html = f'<div class="quiz_container">\n'
        quiz_container = ""
        for idx, quiz in enumerate(quiz_data):
            question_html = f"<h3>{idx+1}. {apply_code_tags(quiz['question'])}</h3>"
            if quiz['code']:
                code_html = f"<pre><code class='language-python'>{quiz['code']}</pre></code>"
            else:
                code_html = ""
            options_html = ""
            for opt_idx, option in enumerate(quiz['options']):
                input_type = 'radio'
                input_name = f"quiz-{idx}"
                input_id = f"{input_name}-option-{opt_idx}"
                options_html += (
                    f'<div>'
                    f'<input type="{input_type}" id="{input_id}" name="{input_name}" value="{opt_idx+1}">'
                    f'<label for="{input_id}">{apply_code_tags(option)}</label>'
                    f'</div>'
                ) 
            explanation_html = f"<div class='explanation' style='display:none;'>{apply_code_tags(quiz['explanation'])}</div>"

            this_question = (
                f'<div class="question" data-correct-answer="{quiz["answer"]}">'
                f'<fieldset>'
                f'{question_html}'
                f'{code_html}'
                f'<form>'
                f'{options_html}'
                f'{explanation_html}'
                f'<button type="submit">Submit</button>'
                f'</fieldset>'
                f'</div>'
            )

            quiz_container += this_question + "\n"
                
        quiz_html += quiz_container
        quiz_html += "</div>"
        return quiz_html

    # @env.macro
    # def show_questions(page_title, filename):
    #     print(page_title + " " + filename)
    #     return f"Page Title: {page_title}, Filename: {filename}"
    
    @env.macro
    def show_questions(page_title, filename):
        if not filename:
            return "Filename not provided"
        
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            return f"{filename} not found"
        except json.JSONDecodeError:
            return f"Error decoding the JSON file {filename}"

        for topic, questions in data.items():
            if topic == page_title:
                return render_quiz(questions)

        return f"Problem showing the questions for topic: {page_title}"

#     @env.macro
#     def get_questions(page_title):
#         instructions = '''
# Select the correct options from the following set of multiple choice questions. Where relevant, try out the commands using the interactive environment or by writing a short Python program to demonstrate.
#         '''
        
#         def apply_code_tags(text):
#         # This function finds text enclosed in backticks and wraps it with <code> tags
#             return re.sub(r'`([^`]*)`', r'<code>\1</code>', text)

#         with open('_data/python_questions.json', 'r') as file:
#             data = json.load(file)
        
#         markdown_content = ""
#         opts = ['a', 'b', 'c', 'd']
#         for topic, questions in data.items():
#             if topic == page_title:
#                 markdown_content += f"{instructions}\n\n"
#                 count = 1
#                 for question in questions:
#                     markdown_content += "<?quiz?>\n"
#                     question_text = apply_code_tags(question['question'])
#                     markdown_content += f"question: {count}. {question_text}\n"
#                     # Add the code snippet if it exists
#                     # if question.get('code'):
#                     if question['code']:
#                         code_snippet = question['code']
#                         markdown_content += "code:\n"
#                         # markdown_content += f"```python\n{code_snippet}\n```\n"
#                         markdown_content += f"{code_snippet}\n"
                        
#                     correct_answer = question['answer']
#                     if question['options']:
#                         for i, option in enumerate(question['options']):
#                             option_text = apply_code_tags(option)
#                             # correct = " correct: true" if option == question.get('correct') else ""
#                             option_label = "answer-correct: " if i+1 == correct_answer else "answer: "
#                             # markdown_content += f"    - option: {option}{correct}\n"
#                             markdown_content += f"{option_label} {option_text}\n"
#                     count += 1
#                     markdown_content += "content:\n"
#                     explanation_text = apply_code_tags(question['explanation'])
#                     # markdown_content += f"{question['explanation']}"
#                     markdown_content += f"{explanation_text}"
#                     # if question['explanation']:
#                     #     markdown_content += f"{question['explanation']}\n"
#                     # else:
#                     #     markdown_content += f"An explanation for the correct answer needs to be added here\n"
#                     markdown_content += "<?/quiz?>\n"
        
#         return markdown_content

    @env.macro
    def get_programming_tasks(page_title):
        
        def make_card(task):
            card_html = "<div class='card'>"
            card_html += "<div class='card-title'>"
            card_html += f"{task['title']}"
            card_html += "</div>"
            if task['outline']:
                card_html += "<div class='card-outline'>"
                card_html += f"<p>{task['outline']}</p>"
                card_html += "</div>"
                card_html += "<div class='card-button'>Read more ...</div>"
            card_html += "</div>"
            return card_html

        instructions = "For each of the following tasks write a program using Python."
        with open('_data/python_tasks.json', 'r') as file:
            data = json.load(file)
        html = ""
        for topic, tasks in data.items():
            if topic == page_title:
                html += f"{instructions}\n"
                if tasks:
                    html += "<div class='card-container'>"
                    for task in tasks:
                        html += make_card(task)
                    html += "</div>"
        return html

    @env.macro
    def get_topics():

        def make_card(topic):
            card_html = "<div class='card'>"
            card_html += "<div class='card-image'>"
            card_html += "<img src=" + topic["image"] + " />"
            card_html += "</div>"
            # card_html += "<div class='card-topic-title'>"
            # card_html += f"{topic['title']}"
            # card_html += "</div>"
            if topic['description']:
                card_html += "<div class='card-outline'>"
                card_html += f"<p>{topic['description']}</p>"
                card_html += "</div>"
                card_html += f"<div class='card-button'><a href='{topic["url"]}'>{topic['title']}</a></div>"
            card_html += "</div>"
            return card_html

        with open('_data/topics.json', 'r') as file:
            data = json.load(file)
        html = ""
        html += "<div class='card-container'>"
        for topic in data:
            html += make_card(topic)
        html += "</div>"
        return html

    @env.macro
    def get_specification(board, spec):
        html = ""
        html += "<h1>" + board + "</h1>"
        html += "<embed src='" + spec + "' width='500' height='600' type='application/pdf' />"
        html += "<p><a class='md-button' href='" + spec + "' target='_blank'>Download PDF</a></p>" 
        html += "<p>Have we arrived here ..?</p>"

        return html
