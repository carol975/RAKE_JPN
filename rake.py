import string
import unicodedata

import MeCab
from jpn_stop_words import jpn_stop_words


"""
print(len(sent))
print(sent.split())
"""

class Rake:
    def __init__(self):
        self.tagger = MeCab.Tagger("-Owakati")
    
    def remove_punctuation(self,text):
        #Ref : http://prpr.hatenablog.jp/entry/2016/11/23/Python%E3%81%A7%E5%85%A8%E8%A7%92%E3%83%BB%E5%8D%8A%E8%A7%92%E8%A8%98%E5%8F%B7%E3%82%92%E3%81%BE%E3%81%A8%E3%82%81%E3%81%A6%E6%B6%88%E3%81%97%E5%8E%BB%E3%82%8B
        text = unicodedata.normalize("NFKC", text)  # 全角記号をざっくり半角へ置換（でも不完全）

        # 記号を消し去るための魔法のテーブル作成
        table = str.maketrans("", "", string.punctuation  + "「」、。・")
        text = text.translate(table)

        return text
        
    def get_word_score(self, word_list):
        freq = {}
        deg = {}

        for word in word_list:
            freq[word] = (freq.get(word) or 0) + 1
            deg[word] = (deg.get(word) or 0) + 1 + len(word)
    
        scores = {}
        for word in word_list:
            scores[word] = deg[word]/freq[word]
        
        scores = {k:v for k, v in  sorted(scores.items(), key= lambda item: item[1], reverse=True)}
        print(scores)
        return scores
    
    def get_keywords(self, text, limit=0):
        parsed_text = self.tagger.parse(text)
        raw_word_list = self.remove_punctuation(parsed_text).split()
        word_list = [word for word in raw_word_list if word not in jpn_stop_words ]
        
        score_list = self.get_word_score(word_list)
        
        if limit == 0:
            return score_list.keys()
        else:
            return score_list[:limit].keys()
sent = "杉山古墳（すぎやまこふん）は、奈良県奈良市大安寺にある古墳。形状は前方後円墳。大安寺古墳群を構成する古墳の1つ。国の史跡に指定されている（史跡「大安寺旧境内 附 石橋瓦窯跡」のうち）。" 
r = Rake()
print(r.get_keywords(sent))        
        
"""    
    
wakati = MeCab.Tagger("-Owakati")
print(wakati.parse(sent))
print(format_text(wakati.parse(sent)))
sent = format_text(sent)
word_list = wakati.parse(sent).split()
word_list = [word for word in word_list if word not in jpn_stop_words ]


print(word_list)

freq = {}
deg = {}

for word in word_list:
    freq[word] = (freq.get(word) or 0) + 1
    deg[word] = (deg.get(word) or 0) + 1 + len(word)
    
score = {}
for word in word_list:
    score[word] = deg[word]/freq[word]
    
print(freq)
print(deg)
print(score)
"""