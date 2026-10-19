# Releasing the Amazonian Voices clld app

```shell
git clone https://github.com/clld/amazonianvoices
cd amazonianvoices
pip install -e .[test,init]
```

Recreate the database from the CLDF data:
```shell
clld initdb development.ini --cldf ../../amazonianvoices/amazonianvoices-cldf/cldf/cldf-metadata.json --glottolog ../../glottolog/glottolog
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
pg_dump -xO amazonianvoices > amazonianvoices.sql
zip amazonianvoices.sql.zip amazonianvoices.sql
rm amazonianvoices.sql
```

