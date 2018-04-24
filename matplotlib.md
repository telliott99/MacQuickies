#### matplotlib

```
> which pip
/usr/local/bin/pip
>
```

That's the one that came with Homebrew's Python.

`pip install`

- `numpy`
- `cython`
- `matplotlib`

``` python
>>> import matplotlib.pyplot as plt
>>> Y = [1,4,9,16]
>>> plt.scatter(range(len(Y)),Y,s=250,color='r')
<matplotlib.collections.PathCollection object at 0x10c751b90>
>>> plt.savefig('example.png')
>>>
```

[example.png](data/example.png)

`pip install`

- `scipy`

``` python
>>> from scipy import stats
>>> from scipy.stats import norm
>>> norm.cdf(0)
0.5
>>> norm.cdf(2)
0.97724986805182079
>>>
```

It's strange.  Over the years, I spent many, many hours building matplotlib and scipy and wrestling with how to get `libpng` available and so on, and now, it just works.  I love it.