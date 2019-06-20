# ponzi

_pixels fit for a pyramid_

Ponzi is an experiment in starting a fresh controller project for the Pyramid.

It currently contains just a `color` package, a port to Python of the excellent
[go-colorful][colorful] library for Go.

[colorful]: https://github.com/lucasb-eyer/go-colorful

## Environment

Ponzi is developed against Python 3.7.3, using [poetry][poetry].

```sh
# Install Python 3 (any method will do)
brew install python
export PATH="$(brew --prefix python)/libexec/bin:${PATH}"

# Install Poetry
curl -fsSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python

# Install dependencies
poetry install

# Play around with the color package
poetry run python
```

[poetry]: https://poetry.eustace.io/
