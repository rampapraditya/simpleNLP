# urutan kerja
# 1 string
# 2 cleaning
# 3 streaming (konversi menjadi kata dasar)
# 4 tokeninzing (merubah ke dalam bentuk array)
# 5 stopword (membuang kata yang tidak perlu)
# 6 end (ditribusi frekuensi)

import requests
import string
import re

from bs4 import BeautifulSoup
import nltk
from nltk.corpus import stopwords
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

import matplotlib.pyplot as plt

# mendapatkan string dan cleaning
web = requests.get("https://nasional.kompas.com/read/2024/04/18/07322321/beragam-respons-kubu-prabowo-gibran-soal-amicus-curiae-megawati-dan-sejumlah").text
soup = BeautifulSoup(web, "html.parser")
for s in soup(['script', 'style']):
    s.decompose()

teks = ' '.join(soup.stripped_strings)
print(teks)

teks = teks.lower()
teks = re.sub(r"\d+", "", teks)
teks = teks.translate(str.maketrans("", "", string.punctuation))
teks = teks.strip()

factory = StemmerFactory()
stemmer = factory.create_stemmer()
output = stemmer.stem(teks)
print(output)

tokens = [t for t in output.split()]
print(tokens)

# nltk.download()
clean_token = tokens[:]
for token in tokens:
    if token in stopwords.words('indonesian'):
        clean_token.remove(token)

freq = nltk.FreqDist(clean_token)
for key, val in freq.items():
    print(str(key) + " : " + str(val))

freq.plot(30)
