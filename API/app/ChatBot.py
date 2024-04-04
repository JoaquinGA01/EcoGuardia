import vertexai
from vertexai.language_models import ChatModel, InputOutputTextPair

vertexai.init(project="totemic-ally-419020", location="us-central1")
chat_model = ChatModel.from_pretrained("chat-bison")
parameters = {
    "candidate_count": 1,
    "max_output_tokens": 1024,
    "temperature": 0.9,
    "top_p": 1
},
safety_settings={ 
          generative_models.HarmCategory.HARM_CATEGORY_HATE_SPEECH: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
          generative_models.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
          generative_models.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
          generative_models.HarmCategory.HARM_CATEGORY_HARASSMENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    }
chat = chat_model.start_chat(
    context="""Eres un experto en el área ambiental con todo tipo de conocimientos para tratamiento de agua, conocimientos de tratamientos de distintas áreas relacionadas con ambiental, y principalmente eres un experto en botánica y el cómo cuidar y mantener en buen estado todo tipo de plantas, sin importar la ubicación. tienes que ser ayudante para personas expertas en el área o guiar a personas que no tienen una idea, ayudando a dar las mejores técnicas dependiendo del contexto en el que se encuentre la persona que necesite ayuda. Solo respondes preguntas en el contexto de botánica y consejos sobre ellas.
el usuario te puede mandar imágenes, preguntar sobre cualquier cosa relacionada con la botánica y tú tienes que darle consejos y buenas técnicas para mejorar el cuidado de estas.
Enfoca que únicamente en esta área de botánica
no respondas preguntas fuera del área de botánica
hazlo un con tono natural y un estilo tranquilo.""",
    examples=[
        InputOutputTextPair(
            input_text="""Hola""",
            output_text="""Hola, ¿Que Tal?, ¿En qué puedo ayudarte?"""
        )
    ]
)
response = chat.send_message("""Hola""", **parameters)
print(f"Response from Model: {response.text}")
response = chat.send_message("""Puedes ayudarme en otro tema que no sea la botanica""", **parameters)
print(f"Response from Model: {response.text}")
response = chat.send_message("""Puedes explicarme que es la fotosintesis?""", **parameters)
print(f"Response from Model: {response.text}")
response = chat.send_message("""Puedes decirme que tipo de plantas son buenas para mi ubicacion actual?""", **parameters)
print(f"Response from Model: {response.text}")