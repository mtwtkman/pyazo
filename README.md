# Pyazo
Gyazo API client implemented by python.

# Required
requests

Gyazo access token.

(You can register your application from [here](https://gyazo.com/oauth/applications).)

# Install

from pypi

```
pip install pyazo
```

# Usage
```
from pyazo import Pyazo
p = Pyazo('MYACCESSTOKEN', client_id='MYCLIENT_ID')
# get images
p.images()

# upload image
p.upload('path/to/img.jpg')

# delete image
p.delete('image_id')

# get oEmbed url
p.oembed('image.url')

# upload with Gyazo session(requires client_id)
p.upload_easy_auth('image.url', 'referer.url')
```

Gyazo API detail is [here](https://gyazo.com/api/docs).
