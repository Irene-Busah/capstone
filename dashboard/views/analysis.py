import openai

openai.api_key = "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"


def generate_data_analysis(data):
    """
    Generate an analysis of the provided data using the new OpenAI API interface.
    """
    # Construct the prompt for data analysis
    prompt = f"Analyze the following data and provide insights(just 4-5 sentences without numbering):\n{data}"

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a data analyst. Provide insights."},
            {"role": "user", "content": prompt},
        ],
    )

    # Extract the response text
    analysis = response["choices"][0]["message"]["content"].strip("\n")
    return analysis


def generate_suggestions(data):
    """
    Generate suggestions based on the provided data using the new OpenAI API interface.
    """
    # Construct the prompt for suggestions
    prompt = f"Based on the following data, suggest actions to improve business performance(just 4 pointsff):\n{data}"

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are a business consultant. Provide suggestions for improvement.",
            },
            {"role": "user", "content": prompt},
        ],
    )

    # Extract the response text
    suggestions = response["choices"][0]["message"]["content"].strip("\n")
    return suggestions
