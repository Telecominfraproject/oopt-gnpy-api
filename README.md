# GNPy API
[![Python versions](https://img.shields.io/pypi/pyversions/gnpy)](https://pypi.org/project/gnpy/)

REST API (experimental)
-----------------------
``gnpyapi`` provides an experimental api for requesting several paths at once. It is based on Flask server.
You can run it through command line or Docker.



    $ curl --location 'http://localhost:8080/api/v1/path-request' --header 'Content-Type: application/json' --data @gnpyapi/exampledata/planning_demand_example.json 

TODO: api documentation, unit tests, real WSGI server with trusted certificates

## Quick Start

tbd