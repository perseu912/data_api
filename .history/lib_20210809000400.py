from __future__ import unicode_literals
import youtube_dl
from googlesearch import search

def get_music_yt(q:str,path:str):
   # ydl_opts =  {'ottmpl': 'music.%(ext)s','postprocessors': [{'key': 'FFmpegExtractAudio','preferredcodec': 'mp3','preferredquality': '192'}]} 
    
    search_q = f'youtube music audio {q}'
    results_term = search(q)
    
    link_result = results_term[0]
    
    import youtube_dl


    ydl_opts = {
    	'outtmpl': f'{path}.%(ext)s',
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
       ydl.download([link_result])
        
    
    return {'link':link_result,
            'path':path
            }

get_music_yt('clubbed of death')
#print(get_music_yt('telephone'))
