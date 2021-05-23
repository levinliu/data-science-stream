# Matplotlib 分享

## 安装后快速使用
```sh
python demo.py
```

## 定制并绘制一条折线图
```sh
python demo1.py
```
## 绘制多条折线图
```sh
python demoN.py
```

## 绘制多款散点图
```sh
python demo_scatter.py
```

## 切换backend
```sh
python demo_bkend.py
```

## 可能出现的问题
```python
(.venv) ➜  lecture02 git:(main) ✗ python demo0.py 
Traceback (most recent call last):
  File "demo01.py", line 1, in <module>
    import matplotlib.pyplot as plt
  File "/Users/mac/python/datas/data-science-stream/.venv/lib/python3.8/site-packages/matplotlib/pyplot.py", line 2500, in <module>
    switch_backend(rcParams["backend"])
  File "/Users/mac/python/datas/data-science-stream/.venv/lib/python3.8/site-packages/matplotlib/pyplot.py", line 277, in switch_backend
    class backend_mod(matplotlib.backend_bases._Backend):
  File "/Users/mac/python/datas/data-science-stream/.venv/lib/python3.8/site-packages/matplotlib/pyplot.py", line 278, in backend_mod
    locals().update(vars(importlib.import_module(backend_name)))
  File "/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/importlib/__init__.py", line 127, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "/Users/mac/python/datas/data-science-stream/.venv/lib/python3.8/site-packages/matplotlib/backends/backend_qt5agg.py", line 11, in <module>
    from .backend_qt5 import (
  File "/Users/mac/python/datas/data-science-stream/.venv/lib/python3.8/site-packages/matplotlib/backends/backend_qt5.py", line 13, in <module>
    import matplotlib.backends.qt_editor.figureoptions as figureoptions
  File "/Users/mac/python/datas/data-science-stream/.venv/lib/python3.8/site-packages/matplotlib/backends/qt_editor/figureoptions.py", line 11, in <module>
    from matplotlib.backends.qt_compat import QtGui
  File "/Users/mac/python/datas/data-science-stream/.venv/lib/python3.8/site-packages/matplotlib/backends/qt_compat.py", line 179, in <module>
    raise ImportError("Failed to import any qt binding")
ImportError: Failed to import any qt binding
```

使用pip install PyQt5
参考：https://stackoverflow.com/questions/52346254/importerror-failed-to-import-any-qt-binding-python-tensorflow


