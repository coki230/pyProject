import pyaudio
import wave
from tqdm import tqdm
import sounddevice as sd
import threading
from queue import Queue
import random
import whisper
import os
import msg_util


class Audio():
    def __init__(self):
        self.CHUNK = 1024
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 1
        self.RATE = 44100
        self.PYAUDIO = None
        self.STREAM = None
        self.audio_list = Queue()
        self.lock = threading.Lock()
        self.model = whisper.load_model("base")
        self.msg_util = msg_util.MsgUtil()

    def get_and_set_PyAudio(self):
        if self.PYAUDIO is None:
            self.PYAUDIO = pyaudio.PyAudio()
        return self.PYAUDIO

    def get_stereo_mix_stream(self):
        device_index = self.get_device_index()
        return self.get_stream(device_index)

    def get_stream(self, device_index=None):
        p = self.get_and_set_PyAudio()
        if device_index:
            self.STREAM = p.open(format=self.FORMAT,
                                 channels=self.CHANNELS,
                                 rate=self.RATE,
                                 input_device_index=device_index,
                                 input=True,
                                 frames_per_buffer=self.CHUNK)
        else:
            self.STREAM = p.open(format=self.FORMAT,
                                 channels=self.CHANNELS,
                                 rate=self.RATE,
                                 input=True,
                                 frames_per_buffer=self.CHUNK)
        return self.STREAM

    def get_out_stream(self, device_index=None):
        p = self.get_and_set_PyAudio()
        if device_index:
            self.STREAM = p.open(format=self.FORMAT,
                                 channels=self.CHANNELS,
                                 rate=self.RATE,
                                 output_device_index=device_index,
                                 output=True,
                                 frames_per_buffer=self.CHUNK)
        else:
            self.STREAM = p.open(format=self.FORMAT,
                                 channels=self.CHANNELS,
                                 rate=self.RATE,
                                 output=True,
                                 frames_per_buffer=self.CHUNK)
        return self.STREAM

    def put_record_to_list(self):
        file = "".join(random.sample('zyxwvutsrqponmlkjihgfedcba', 7)) + ".wav"
        self.save_file(file, 10)
        self.audio_list.put(file)

    def deal_file(self):
        # self.lock.locked()
        file_name = self.audio_list.get()
        result = self.model.transcribe(file_name)
        os.remove(file_name)
        print(result["text"])
        noun_words = self.msg_util.get_noun(result["text"])
        self.msg_util.find_file(noun_words)
        # self.lock.release()

    def save_file(self, wave_out_path, record_second):
        device_index = self.get_device_index()
        stream = self.get_stream(device_index)
        wf = wave.open(wave_out_path, 'wb')
        wf.setnchannels(self.CHANNELS)
        wf.setsampwidth(self.get_and_set_PyAudio().get_sample_size(self.FORMAT))
        wf.setframerate(self.RATE)

        print("* recording")

        for i in tqdm(range(0, int(self.RATE / self.CHUNK * record_second))):
            data = stream.read(self.CHUNK)
            wf.writeframes(data)

        print("* done recording")
        stream.stop_stream()
        wf.close()

    def record_audio(self, wave_out_path, record_second):
        self.save_file(wave_out_path, record_second)
        self.close()

    def get_device_index(self):
        list = sd.query_devices()
        for item in list:
            if item['hostapi'] == 0:
                if item["name"] == 'Stereo Mix (Realtek(R) Audio)' and item['hostapi'] == 0:
                    return item["index"]

    def close(self):
        if self.STREAM is not None:
            self.STREAM.close()
        if self.PYAUDIO is not None:
            self.PYAUDIO.terminate()

# record_audio("output.wav", record_second=10, device_index=1)
