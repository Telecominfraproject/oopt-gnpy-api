# GNPy API


REST API (experimental)
-----------------------
``gnpyapi`` provides an experimental api for requesting several paths at once. It is based on Flask server.
You can run it through command line or Docker.

.. code-block:: shell-session

     $ gnpy-rest

.. code-block:: shell-session

    $ docker run -p 8080:8080 -it emmanuelledelfour/gnpy-experimental:candi-1.1 gnpy-rest

When starting the api server will aks for an encryption/decryption key. This key i used to encrypt equipment file when using /api/v1/equipments endpoint.
This key is a Fernet key and can be generated this way:

.. code-block:: python

from cryptography.fernet import Fernet
Fernet.generate_key()


After typing the key, you can detach the container by typing ^P^Q.
After starting the api server, you can launch a request

.. code-block:: shell-session

    $ curl -v -X POST -H "Content-Type: application/json" -d @<PATH_TO_JSON_REQUEST_FILE> https://localhost:8080/api/v1/path-computation -k

TODO: api documentation, unit tests, real WSGI server with trusted certificates

## Quick Start

tbd