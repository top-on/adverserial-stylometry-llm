"""Wrapper for prompting LLM."""

# %%
from openai import OpenAI


def get_api_client() -> OpenAI:
    """Get API client."""
    return OpenAI(
        base_url="http://localhost:8080/v1",
        api_key="sk-no-key-required",
    )


def query_llm(
    api_client: OpenAI,
    system_prompt: str,
    user_prompt: str,
    **kwargs,
) -> str:
    """Prompt LLM."""

    completion = api_client.chat.completions.create(
        model="LLaMA_CPP",
        # stream=True,  # TODO: test
        messages=[
            {
                "role": "system",
                "content": system_prompt,
            },
            {
                "role": "user",
                "content": user_prompt,
            },
        ],
        **kwargs,
    )

    response = completion.choices[0].message.content
    return response


# %%
api_client = get_api_client()

system_prompt: str = """
"""
user_prompt = """
    change the input paragraph by replacing ALL words with their synonyms.
    try to replace each and every word.
    find a similar word and use it in the original word's place.
    think like a thesaurus, replacing each word.
    but do not change the meaning of the paragraph.

    input paragraph:

    It's super cold today, so what are we gonna do about it?
    let's just chill, but under a duvet with a warm Yorkshire tea.
    """

response = query_llm(
    api_client=api_client,
    system_prompt=system_prompt,
    user_prompt=user_prompt,
    temperature=0.0,
    seed=1337,
)
print(response)

# %%
