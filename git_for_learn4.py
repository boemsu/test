import os,sys
sys.path.append(os.pardir)
import openpyxl as op

# f = open("for_learn.txt", "w")
# f.write("Hellow World")
# f = open("for_learn.txt", "r")
# line = f.read()
# print(line)

import zipfile

file_path = "C:/AI_Npc/스토리.total.zip"
file_name = "스토리"

def load_conversations(file_path, file_name):
    conversations = []
    with zipfile.ZipFile(file_path, 'r') as zip_file:
        for file in zip_file.namelist():
            if file.encode('cp437').decode('euc-kr').startswith(file_name):
                with zip_file.open(file, 'r' ) as file_obj:
                    lines = file_obj.readlines()
                    for line in lines:
                        conversation = line.decode('utf-8').strip().split('\t')
                        conversations.append(conversation)
    return conversations

conversations = load_conversations(file_path, file_name)

input_texts = []
target_texts = []
sentence_last = 'garbage'

for conversation in conversations:
    for i in range(len(conversations)):
        for sentence in conversations[i]:
            if sentence.startswith('B'):
                input_texts.append(sentence)
                if sentence_last.startswith('B'):
                    input_texts.append(sentence_last + sentence)
                    input_texts.remove(sentence_last)
                    input_texts.remove(sentence)
            elif sentence.startswith('A'):
                target_texts.append(sentence)
                if sentence_last.startswith('A'):
                    target_texts.append(sentence_last + sentence)
                    target_texts.remove(sentence_last)
                    target_texts.remove(sentence)
        sentence_last = sentence


print(input_texts)
print(target_texts)

