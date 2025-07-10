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

def suggest_resume_improvements(resume_text):
    prompt = f"""
    You are an AI resume reviewer. Read the resume below and suggest:
    1. Missing key skills or technologies
    2. Revisions to make statements more impactful and quantifiable if possible
    """
    response = openai.responses.create(
        model="gpt-4o-mini",
        instructions=prompt,
        input=resume_text
    )
    return response.output_text