from langchain_core.prompts import ChatPromptTemplate


# Template for generating an email
template_generate = ChatPromptTemplate.from_messages([
    (
        "system",
        """
        You are a professional email assistant.

        Generate an email using the information provided.
        Return ONLY a valid JSON object with these keys:
        - recipient
        - subject
        - body

        Do not include Markdown code fences or extra text.
        """
    ),
    (
        "human",
        """
        Recipient: {recipient}
        Sender: {user}
        Tone: {tone}
        Subject: {subject}
        """
    )
])


# Template for rewriting an email
template_rewrite = ChatPromptTemplate.from_messages([
    (
        "system",
        """
        You are an expert email editor.
        Rewrite emails according to the requested tone.
        Preserve the original meaning and important details.
        Return only the rewritten email.
        """
    ),
    (
        "human",
        """
        Rewrite the following email in a {tone} tone:

        {email}
        """
    )
])
