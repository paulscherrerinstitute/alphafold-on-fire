# alphafold-on-fire backend

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat)](https://pycqa.github.io/isort/)

---
## Project structure
```console
.
├── app  # src for the application
│   ├── config.py  # reading in settings from env
│   ├── database.py  # configuring database connection
│   ├── main.py  # main entrypoint for the application
│   ├── routers  # route definitions
│   └── schemas  # pydantic model definitions
└── tests  # tests
```
