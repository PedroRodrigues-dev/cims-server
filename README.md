# Cloud Infrastructure Management System Server - CIMS-SERVER

## tools

- python 3.11.2
- rabbitMQ 3.11.10

## Development

1. Install ASDF:

   follow this guide <https://asdf-vm.com/guide/getting-started.html>

2. Add python plugin:

   asdf plugin-add python

3. Install python:

   asdf install python 3.11.3

4. Create venv:

   python -m venv env

5. Activate venv:

   source env/bin/activate

6. Install dependencies:

   pip install -r requirements.txt

7. Define environment variables:

   export CIMS_SERVER_SERVER_NAME=Your server name (required)

   export CIMS_SERVER_RABBIT_USERNAME=guest (default)

   export CIMS_SERVER_RABBIT_PASSWORD=guest (default)

   export CIMS_SERVER_RABBIT_HOST=localhost (default)

8. Run application:

   python main.py

## Production

1. Define environment variables:

   export CIMS_SERVER_SERVER_NAME=Your server name (required)

   export CIMS_SERVER_RABBIT_USERNAME=guest (default)

   export CIMS_SERVER_RABBIT_PASSWORD=guest (default)

   export CIMS_SERVER_RABBIT_HOST=localhost (default):

2. Untar applciation:

   tar -xvf cims-server-buildVersion

3. Run application:

   ./main

## Generate Package

1. Access generatePackage.sh:

   change the version variable to your version

2. Run generatePackage.sh:

   ./generatePackage.sh

3. Upload version to github:

   follow the model that was used for the other releases and tags
