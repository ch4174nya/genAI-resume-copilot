import openai

def rewrite_resume_line(line):
    prompt = f"""
    You are a resume optimization assistant. Rewrite this bullet point to make it clearer, more impactful and quantifiable if possible.
    """
    response = openai.responses.create(
        model="gpt-4o-mini",
        instructions=prompt,
        input=line
    )
    return response.output_text