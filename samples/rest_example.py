#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
gnpy.tools.rest_example
=======================

GNPy as a rest API example
'''

import argparse
import logging
import tempfile
from logging.handlers import RotatingFileHandler

import uvicorn
from OpenSSL import crypto

from gnpyapi.core import app

_logger = logging.getLogger(__name__)


def _init_logger():
    handler = RotatingFileHandler('api.log', maxBytes=1024 * 1024, backupCount=5, encoding='utf-8')
    ch = logging.StreamHandler()
    logging.basicConfig(level=logging.INFO, handlers=[handler, ch],
                        format="%(asctime)s %(levelname)s %(name)s(%(lineno)s) [%(threadName)s - %(thread)d] - %("
                               "message)s")


def _create_adhoc_ssl_files():
    temp_dir = tempfile.TemporaryDirectory()
    key = crypto.PKey()
    key.generate_key(crypto.TYPE_RSA, 2048)

    cert = crypto.X509()
    cert.get_subject().CN = "localhost"
    cert.set_serial_number(1)
    cert.gmtime_adj_notBefore(0)
    cert.gmtime_adj_notAfter(365 * 24 * 60 * 60)
    cert.set_issuer(cert.get_subject())
    cert.set_pubkey(key)
    cert.sign(key, "sha256")

    cert_path = f"{temp_dir.name}/adhoc-cert.pem"
    key_path = f"{temp_dir.name}/adhoc-key.pem"
    with open(cert_path, "wb") as cert_file:
        cert_file.write(crypto.dump_certificate(crypto.FILETYPE_PEM, cert))
    with open(key_path, "wb") as key_file:
        key_file.write(crypto.dump_privatekey(crypto.FILETYPE_PEM, key))
    return temp_dir, cert_path, key_path


def main(http: bool = False):
    _init_logger()

    if http:
        uvicorn.run(app, host='0.0.0.0', port=8080, log_config=None)
    else:
        temp_dir, cert_path, key_path = _create_adhoc_ssl_files()
        try:
            uvicorn.run(app, host='0.0.0.0', port=8080, ssl_certfile=cert_path, ssl_keyfile=key_path,
                        log_config=None)
        finally:
            temp_dir.cleanup()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Rest API example")

    parser.add_argument("--http", action="store_true", help="run server with http instead of https")

    args = parser.parse_args()

    main(http=args.http)
