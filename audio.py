import requests
import subprocess
from playsound import playsound

filename = 'audio.m4a'

doc = requests.get("https://d6h3ltzwkim1h.cloudfront.net/216b9d6d-face-4ab5-948f-8c44ead27a08/216b9d6d-face-4ab5-948f-8c44ead27a08.m4a?Expires=1657852555&Key-Pair-Id=APKAIG2AUVCADBSUVKSQ&Signature=NRTB6XmQUuHFu7ihiC7c0El-7OrEmc238ArPG3-gH-3b7u558uo6ALEOk8tEXnVnZ6ETElI0lDB89gg2AYQ%7ETp35QogPCAe5UD58TSJpApeubiZQzJF62%7EMPyze2nnpRDG85wjrkAWy1xwy-4h1WA6tLxgMo-re7NoqGpEH87IZXsxG%7ElAHC-9yMDmlyXG3gCgbuCPrOx41N8nFEMuvpdsHWEUZ%7ECQktmTPVPSpXRNC5wvH-etn3HV2nsqS5oGw8L1SI9b9la-xIU7J0wOzxzs58LD4m9Rr-3VNowNSz0er2R7%7EbCVyo33dUXAgR22wKXnYNogk2hjeXEWFq2bESlA__")

with open(filename, 'wb') as f:
    f.write(doc.content)

playsound('./audio.m4a')
