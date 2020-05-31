A simple picture meme generator built on Flask and PIL libraries.

## Requirements

Picture format must be PNG.

Backgrounds must be 500 x 500.

Foreground images must be 250x250.


## Usage

create Python3 virtual env and activate it
```
python3 -m venv venv && . venv/bin/activate
```

Set your application environment variable script.
```export FLASK_APP=flask_site.py```

Set debug on (if you want to test live without server reloads)
```export FLASK_DEBUG=1```

Run Flask locally
```buildoutcfg
flask run
```


Run Flask in docker allowing external access to the device (otherwise only localhost works)
```buildoutcfg
docker run -p 5000:5000 tnielsen2/memegenerator flask run --host=0.0.0.0
```
