# Tulpar
[![security: bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)
[![linting: pylint](https://img.shields.io/badge/linting-pylint-yellowgreen)](https://github.com/PyCQA/pylint)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)



Python SSR Framework built on Falcon, PonyORM, and HTMX

## Overview

Tulpar is a Python Web Framework built on top of Falcon and PonyORM, with the communication being strictly HATEOAS. This means that all communication is through HTML, and therefore through Jinja templates. To communicate with the backend, and provide a SPA-like experience, HTMX is introduced. 

## Layout of an Application
A Tulpar application has a specific layout.
```
<App>/
  | base.html <-- Base Template
  | config.py <-- Tulpar config file
  | app.py    <-- Main Application File
  pages/
  resources/
  assets/
  middleware/
  hooks/
  orm/
   | models.py
```
Each serve a purpose.
### Pages
The pages directory is where main page application files go. This is where something like an About Me page would be.

In the future I would like to introduce a HTML DSL for writing pages, but as of now they are simply Falcon Resources. They must implement a `on_get` method for the page to work. 

### Resources
Resources are api endpoints that serve up HTML. These are decorated with `@Resource`.
```python
@Resource("/")
class X:
    def on_get(self, req: Request, res: Response) -> HTML:
        return HTML("<p>Hello World</p>")
```

### Assets
These are the static assets and are served up as a static directory.

### Middleware and Hooks
These are ways to implement Falcon Hooks and Middleware in a Tulpar application.

### ORM
This is where your PonyORM models are stored.
```python
class Book(Tulpar.db.Entity):
    ...
```