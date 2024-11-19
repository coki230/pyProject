import brain

# while True:
#     vt = seepk2text.get_voice_text()
#
#     res = brain.response(vt)
#
#     text2voice.text2voice(res)


res = brain.response("what are your name?")
print(res)
# text2voice.text2voice(res)

res = brain.response("what is Scrapy?")
print(res)
# text2voice.text2voice(res)
#
# res = brain.response("how old are you?")
# print(res)
# # text2voice.text2voice(res)