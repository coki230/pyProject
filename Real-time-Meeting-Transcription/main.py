import audio_util as au
from concurrent.futures import ThreadPoolExecutor

# audio = au.Audio()
# stream = audio.get_stereo_mix_stream()
# pool = ThreadPoolExecutor(5)
#
# def check(t):
#     result = t.result()
#     print(result)
#
# while True:
#     audio.put_record_to_list()
#     pool.submit(audio.deal_file).add_done_callback(check)


# audio.record_audio("output.wav", record_second=10)


audio = au.Audio()
stream = audio.get_out_stream(23)
audio.record_audio("output.wav", record_second=10)
