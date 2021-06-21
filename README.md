# Install

```bash
> pip install sekte2pdf
```

# Python Interpreter
## Save To File
```python
>>> import sekte
>>> x=sekte.search('fairy').fetch
>>> x[2].download(chapter=1)
>>> x.save_to_file('filename.pdf')
```
## BytesIO
 ```python
 >>> import sekte
>>> x=sekte.search('fairy').fetch
>>> x[2].download(chapter=1)
```
## ByUrl
```python
>>> import sekte
>>> x=Sekte('https://sektekomik.com/manga/i-become-a-fairy/').manga
>>> x.json
```
