import ollama
# response = ollama.chat(model='llama3.2', messages=[
#   {
#     'role': 'user',
#     'content': 'Why is the sky blue?',
#   },
# ])
# print(response['message']['content'])

# def response(input_content):
#   response = ollama.chat(model='llama3.2', messages=[
#     {
#       'role': 'user',
#       'content': input_content,
#     },
#   ])
#   return response['message']['content']


# from langchain_ollama import OllamaLLM
#
# prompt = "give me a brief answer as short as possible, just like two people talk, "
# "and you are a teacher to teach me English. If I have some grammatical errors in my"
# "previous answer or response, please point them out and correct it<|eot_id|><|start_header_id|>assistant<|end_header_id|>"
# ollama = OllamaLLM(
#     base_url='http://localhost:11434',
#     model="llama3.2"
# )
#
# def response(input_content):
#     return ollama.invoke(prompt + input_content)
#
#
# while True:
#     txt = input("pls input.")
#     print(ollama.invoke(txt))


# import ollama
#
# def response(input_content):
#     return ollama.chat(model='llama3.2', messages=[{
#         'role': 'user',
#         'content': input_content
#     }])



from ollama import Client

ollama = Client(host='my.ollama.host')


def response(input_content):
    ollama.generate(
        model='llama3.2',
        messages=[{
            'role': 'user',
            'content': input_content
        }])



while True:
    txt = input("pls input.")
    print(response(txt))