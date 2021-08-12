from __future__ import unicode_literals
import youtube_dl
from googlesearch import search

def get_music_yt(q:str):
    ydl_opts =  {'postprocessors': [{'key': 'FFmpegExtractAudio','preferredcodec': 'mp3','preferredquality': '192'}]} 
    
    search_q = f'youtube {q}'
    results_term = search(q)
    
    link_result = results_term[0]
    return link_result


print(get_music_yt('clubbed of death'))