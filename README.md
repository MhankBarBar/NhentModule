[![CodeQL](https://github.com/MhankBarBar/SekteModule/actions/workflows/codeql-analysis.yml/badge.svg?branch=master)](https://github.com/MhankBarBar/SekteModule/actions/workflows/codeql-analysis.yml)
# Install

```bash
> pip install sekte2pdf
```

# Python Interpreter
## Save To File
```python
>>> import sekte
>>> x=sekte.Search('fairy').fetch[2]
>>> x.download(chapter=1)
>>> x.save_to_file('filename.pdf')
```
## BytesIO
 ```python
 >>> import sekte
>>> x=sekte.Search('fairy').fetch[2]
>>> x.download(chapter=1)
```
## ByUrl
```python
>>> import sekte
>>> x=sekte.Sekte('https://sektekomik.com/manga/i-become-a-fairy/').manga
>>> x.json
```
