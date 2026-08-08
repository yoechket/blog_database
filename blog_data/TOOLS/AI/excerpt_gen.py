import ollama

def generate_excerpt_with_ollama(title, content, categories):
    category_names = ", ".join([cat.name for cat in categories])

    response = ollama.chat(model='llama3.1', messages=[
        {
            "role": "user",
            "content": "Create a 2 phrase summary for:\nTitle:" +\
                f"{title}\nCategories: {category_names}\nContent: {content[:1000]}" + \
                "And remove any introductory sentences such as: Here is a ... summary:"
        }
    ])
    return response['message']['content']
