# Install

```bash
> pip install sekte
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
 >>> import doujin
>>> x=sekte.search('fairy').fetch
>>> x[2].download(chapter=1)
```
