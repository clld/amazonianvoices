# Releasing the Amazonian Voices clld app

```shell
git clone https://github.com/clld/amazonianvoices
cd amazonianvoices
pip install -e .[test]
```

Recreate the database from the CLDF data:
```shell
clld initdb development.ini --cldf ../../amazonianvoices/amazonianvoices-cldf/cldf/cldf-metadata.json --glottolog ../../glottolog/glottolog
```

```shell
pytest
```
