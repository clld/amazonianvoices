# Releasing the Amazonian Voices clld app

```shell
git clone https://github.com/clld/amazonianvoices
git clone --branch v1.0 --depth 1 https://github.com/lexibank/amazonianvoices amazonianvoices-cldf
git clone --branch v5.3 --depth 1 https://github.com/glottolog/glottolog
git clone --branch v2.3.1 --depth 1 https://github.com/cldf-clts/clts
cd amazonianvoices
pip install -e .[test,init]
```

Recreate the database from the CLDF data:
```shell
clld initdb development.ini --cldf ../amazonianvoices-cldf/cldf/cldf-metadata.json --glottolog ../glottolog
```

```shell
pytest
```

Store the tested requirements:
```shell
pip freeze > requirements.txt
```

Store a db dump:
```shell
pg_dump -xO --compress gzip:9 amazonianvoices > amazonianvoices.sql.gz
```

