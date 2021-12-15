# About
This repository contains a reproduction of a bug in CockroachDB's django adapter.

`.filter(field__startswith=value)` queries return an incorrect result
if `value` contains a special character (`_`, `\` or `%`).

The bug was reported in cockroachdb/django-cockroachdb#243

## Requirements
* docker
* docker-compose

## Running repro
```
./run_test.sh
```

To compare to correct behavior swap comments on `DATABASES` definiton in [repro/settings.py](repro/settings.py)