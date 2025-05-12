# GNPy API
[![Install via pip](https://img.shields.io/pypi/v/gnpy-api)](https://pypi.org/project/gnpy-api/)
[![Python versions](https://img.shields.io/pypi/pyversions/gnpy-api)](https://pypi.org/project/gnpy-api/)
[![Gerrit](https://img.shields.io/badge/patches-via%20Gerrit-blue)](https://review.gerrithub.io/q/project:Telecominfraproject/oopt-gnpy-api)

REST API (experimental)
-----------------------
This repository extends GNPy with additional interfaces, allowing for more flexible control and interaction with its simulation engine. These interfaces can be used to integrate GNPy into software-defined networking (SDN) architectures or other external applications.

[GNPy](https://github.com/Telecominfraproject/oopt-gnpy) is an open-source Python-based library that models and evaluates the performance of optical networks. It is widely used for path computation, QoT (Quality of Transmission) estimation, and network planning.

## 🚀 Installation
### Build from Source - Option 1
Clone the repository and install the package:
```bash
python3 setup.py install
```
or if you want to install it in a docker container:
```bash
docker docker build ./ -t gnpy-api
```

### PiPy - Option 2
```bash
pip install gnpy-api
```


### DockerHub - Option 3
Coming.... 
## Quick Start

## 🧪 Usage - CLI
Start the REST API server:
```bash
python ./samples/rest_example.py
```
See the help for the REST API:
```bash
python ./samples/rest_example.py -h
```
Send example data to the REST API:
```bash
curl --location 'https://localhost:8080/api/v0.1/path-request' --header 'Content-Type: application/json' --data @gnpyapi/exampledata/planning_demand_example.json -k
```
## 🧪 Usage - Docker



## 🔄 Compatibility

Different versions of this interface extension are compatible with specific versions of [GNPy](https://github.com/Telecominfraproject/oopt-gnpy). Please refer to the table below to ensure that you are using a supported version combination.



| Interface Version | Compatible GNPy Version | Notes                          |
|-------------------|-----------------|--------------------------------|
| `v0.1.x`          | `>=2.12.1`      | Initial release                |

⚠️ If you use an incompatible combination, some features may not work correctly or may produce unexpected errors.

To check your GNPy version, run:

```bash
pip show gnpy
```

## 📚 Documentation
Refer to the official [GNPy documentation](https://github.com/Telecominfraproject/oopt-gnpy/tree/master/docs) for information about network modeling and simulation capabilities.

API documentation is available in the docs folder.