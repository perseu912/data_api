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
<source src='/mp3/intercooler_dj_jacob.mp3' type='mpeg'>
</audio>