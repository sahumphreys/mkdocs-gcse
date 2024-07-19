# main.py
# -----------------------------------------------------------------
# Additional configuration/processing for GCSE CS site
# =================================================================
import json

def define_env(env):

    @env.macro
    def get_message(n):
        return f"??? Hello\n\t{n}"

    @env.macro
    def get_questions(page_title):
        instructions = '''
Select the correct options from the following set of multiple choice questions.  Where relevant try out the commands using the interactive environment or by writing a short Python program to demonstrate.
        '''
        with open('_data/python_questions.json', 'r') as file:
            data = json.load(file)
        html = ""
        for topic, questions in data.items():
            if topic == page_title:
                html += f"{instructions}\n"
                html += "<ol>"
                if questions:
                    for question in questions:
                        html += "<li class='question'>" + question['question'] + "</li>"
                        if question['options']:
                            html += "<ol>"
                            for option in question['options']:                                
                                html += "<li>" + option + "</li>"
                            html += "</ol>"
                html += "</ol>"
        return f"{html}"

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
