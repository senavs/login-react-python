import io
import re

from setuptools import find_packages, setup

dev_requirements = [
]

run_requirements = [
    'fastapi==0.63.0',
    'uvicorn==0.13.3',
    'gunicorn==20.0.4',
    'SQLAlchemy==1.3.22',
    'mysqlclient==2.0.3',
    'pyjwt==2.0.1',
    'bcrypt==3.2.0'
]

with io.open('./api/__init__.py', encoding='utf8') as version_f:
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_f.read(), re.M)
    if version_match:
        version = version_match.group(1)
    else:
        raise RuntimeError("Unable to find version string.")

setup(
    name="todo",
    version=version,
    author="Matheus Sena Vasconcelos",
    author_email="sena.matheus14@gmail.com",
    packages=find_packages(),
    include_package_data=True,
    url="https://github.com/senavs/todo-list",
    description="To do list WEB application with Python, NodeJS and React.",
    zip_safe=False,
    install_requires=run_requirements,
    extras_require={
        'dev': dev_requirements
    },
    python_requires='>=3.8',
    keywords=()
)
