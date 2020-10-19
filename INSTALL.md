# Universidad de Palermo | Machine Learning | Cartasur

THIS FILE USED TO BE THE README.md, but it was quite hard to keep it up to date since this is something that we change quite a lot based on decisions we made week by week, and sometimes on every commit. So I will keep it as a way to see the installation process and I will make the old `README.md` a sort of "changelog". With all the new features and things we introduced

## Installation

To simplify installation we have decided to use `Makefile`. It is a good ol' tool that can define dependencies graphs easily. So if you want to install dependencies you have to create your own dependencies and requirements

```
make install_osx
```

## Datasets

The datasest must be stored inside the ./data/ directory.

### Sanitize Datasets

The datasets are not sanitized. In order to load them you have to do a few things:

1. You have to remove one weird byte that it's at the beginning of each file.

2. Add the missing column names in all of them. Otherwise it will be impossible for pandas to merge them into a single dataframe.

3. If you are on a `*nix` flavored system you can do this to determine the encoding format: 

``` sh
▶ file data/*csv
data/CLIENTES.csv: ASCII text
data/CREDITOS.csv: ISO-8859 text
data/CUOTAS.csv:   ASCII text
data/PAGOS.csv:    ASCII text
```

Bear in mind that ASCII is included in ISO8859-1 (Latin) and both are included in UTF-8. All python strings are UTF-8 compatible but you need to specify the source data otherwise panda library will fail. That's why you see the encoding set to `ISO8859-1` in the `read_csv`.


## Libraries

We have developed some libraries that could be useful for this project.
These libraries are just to standarize the input data and improve the way the ML algorithm works. For the
sake of organization, all these libraries are included in `./lib`.


### **`normalizer`**

The `normalizer` library is a library we have developed to normalize the input data. Since in ML we can't use strings and it is better to group data into _not unique_ values we have created this `normalizer` libraries as helpers for normalizing our data.

For example if you have values for example amounts. Often you don't care if the value is 1012.25 or 1010 or, even sometimes you want to group into bigger values, like 1100 is the same as 1000.

Also `string` data type is not allowed for ML input algorithms so we need to convert them into numeric values.

For all these kind of things we have created this library, so take a look at the library. We have documented each function of the library so it's easy to use.


## Random Thoughts

This section of the README.md is just to write down random thoughts I am thinking while working on this.

## CREDITOS - MONTO

It is interesting to see that we have amounts from 1 to 204663. The first one doesn't seems to be really useful, I really doubt someone can ask a credit for $1. However, the latter looks more likely to be a real vaule.

```
>>> everything["MONTO"].min()
1.0
>>> everything["MONTO"].max()
204663.0
>>>
```

So I have to count these values to know which ones are interesting to see and perhaps if we need to filter out these columns in some way:

## 2020-10-12

I have added a few elements to cluster the elements using k-means. I still have no results on that, however
I pushed the code because I think it's important to have that for future references.




