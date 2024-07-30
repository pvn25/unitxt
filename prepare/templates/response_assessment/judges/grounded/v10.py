from unitxt import add_to_catalog
from unitxt.templates import InputOutputTemplate

add_to_catalog(
    InputOutputTemplate(
        instruction="""Read the following three parts: (A) Document, (B) Conversation between the user and the agent occurring in multiple turns. The user and agent alternate the conversation where the user asks a question, the agent gives a response to that question, and the user poses an inquiry at the end, (C) the Response (of the agent) to the last turn user query that continues the conversation from part 2. Your task is to evaluate if the statements in the Response (C) are mentioned in the Document without any external knowledge. Your task is to return output in the following format: [one word Judgement]. [Explanation: A concise explanation of how the decision was made].  To do so, first follow these two steps for 'Explanation' part: (1) Exhaustively identify all the assertions and well-known facts contained in the Response. (2) For every identified assertion and well-known fact, state what part of the document make this reference. If the document does not contain the assertion or the facts, state that no explicit reference found in the Document. For 'judgment' output, if you can indeed find mentions of all the assertions and well-known facts in the document, then your judgement should be 'yes'.  If not, your judgement should be 'no'. Even if well-known fact is not explicitly mentioned in the Document then your judgement should be 'no'.""",
        input_format="\n\nConversation:\n{question}\n\nResponse:\n{answer}\n\n\nOutput:",
        output_format="[[{rating}]]",
        postprocessors=[
            r"processors.extract_mt_bench_string_judgment",
        ],
    ),
    "templates.response_assessment.judges.grounded.v10",
    overwrite=True,
)
