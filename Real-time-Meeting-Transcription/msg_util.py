import spacy
import pathlib
import docx


class MsgUtil():
    def __init__(self):
        print("we are init the env now, we now collect all doc file, wait .....")
        self.nlp = spacy.load("en_core_web_sm")
        self.directory = "C:\\Users\\Coki_Zhao\\Desktop\\temp\\"
        self.files = list(pathlib.Path(self.directory).glob("**/*.docx"))
        print("collected all doc file, let do it.")

    def get_noun(self, text):
        doc = self.nlp(text)
        return [chunk.text for chunk in doc.noun_chunks]

    def find_file(self, noun_words):
        for file in self.files:
            document = docx.Document(file)
            keywords = noun_words
            matches = []
            for para in document.paragraphs:
                for keyword in keywords:
                    if keyword.lower() in para.text.lower():
                        matches.append(para.text)
                        print("====================================")
                        print("file", file)
                        print("keyword", keyword)
                        print("text", para.text)
                        print("====================================")
