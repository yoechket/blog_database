import ollama

def generate_excerpt_with_ollama(title, content, categories):
    category_names = ", ".join([cat.name for cat in categories])

    response = ollama.chat(model='llama3.1', messages=[
        {
            'role': 'user',
            'content': f'Create a 3-4 sentence excerpt for:\nTitle: {title}\nCategories: {category_names}\nContent: {content[:1000]}'
        }
    ])
    return response['message']['content']
