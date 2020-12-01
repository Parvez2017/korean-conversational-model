# -*- coding: utf-8 -*-

import pandas as pd 
import glob

root_dir = '/home/ticonsystem/parvej/KoGPT2-chatbot/Chatbot_data/korean_dataset/'
input = []
reply = []

for filename in glob.iglob(root_dir + '**/*.txt', recursive=True):
    with open(filename) as f:
        lines = [line.rstrip('\n') for line in f]
        
    for id in range(0, len(lines), 2):
        input.append(lines[id])
        reply.append(lines[id+1])




df = pd.DataFrame(zip(input, reply), columns=["Q", 'A'])
df.to_csv('korean_merged_processed.csv', index=False)


# Reading and processing the ChatbotData.csv file

df_new = pd.read_csv('ChatbotData.csv')
df_new = df_new.dropna()
df_new = df_new[['Q', 'A']]
df_new.to_csv('chatbot_processed.csv', index=False)

# merging process...
merged = df.merge(df_new, how='outer', on=['Q', 'A'])
merged.to_csv('merged_final.csv', index=False)