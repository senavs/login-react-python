# API
autopep8 api/ --max-line-length 160 --in-place --recursive 2> /dev/null
isort api/. --line-length 160 --py 38 2> /dev/null
flake8 api --config .flake8 --count
