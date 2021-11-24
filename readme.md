# libmusic
## example

```py
from lib import search_gyt as gy
from lib import search_ytdl as sy
from lib import download_yt as dy

res_gy = (gy('intercooler dj jacob'))
print(res_gy)
dy(res_gy[0])
```
output:
<audio controls>
<source src='https://github.com/perseu912/work_api/raw/main/mp3/intercooler_dj_jacob.mp3' type='audio/mpeg'>
Your browser does not support the audio element.
</audio>