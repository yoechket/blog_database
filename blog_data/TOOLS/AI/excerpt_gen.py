import openai

from django.conf import settings


def generate_excerpt_with_ai(title, content, categories):
    """Generate article excerpt using OpenAI GPT"""
    openai.api_key = settings.OPENAI_API_KEY

    category_names = ", ".join([cat.name for cat in categories]) if categories else "Uncategorized"

    prompt = f"""Generate a compelling 2-3 sentence excerpt for this blog article.

Title: {title}
Categories: {category_names}
Content: {content[:1000]}  # First 1000 chars

Create an engaging excerpt that captures the main idea and encourages readers to continue."""

    try:
        response = openai.chat.completions.create(
            model="gpt-4o-mini",  # or "gpt-4" for better quality
            messages=[
                {
                    "role": "system",
                    "content": "You are a professional content\
                        editor creating engaging article excerpts."
                    },
                {"role": "user", "content": prompt}
            ],
            max_tokens=150,
            temperature=0.7
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"Error generating excerpt: {e}")
        return content[:200] + "..."  # Fallback to simple truncation
