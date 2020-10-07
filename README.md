# Universidad de Palermo | Machine Learning | Cartasur

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


