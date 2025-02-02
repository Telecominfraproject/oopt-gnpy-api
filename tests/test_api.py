#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: Esther Le Rouzic
# @Date:   2025-02-03

from pathlib import Path
import subprocess
import pytest   # noqa: F401


YANG_DIR = Path(__file__).parent.parent / 'gnpyapi' / 'yang'
SAMPLE_DIR = Path(__file__).parent.parent / 'samples'


def test_sample():
    """Just for the ci
    """
    res = subprocess.run(['python', SAMPLE_DIR / 'fake_sample.py'],
                         stdout=subprocess.PIPE, check=True)
    if res.returncode != 0:
        assert False, f'gnpy call failed: exit code {res.returncode}'


def test_pyang():
    """Verify that yang models pss pyang
    """
    res = subprocess.run(['pyang', '-f', 'tree', '--tree-line-length', '69',
                          '-p', YANG_DIR, YANG_DIR / 'gnpy-api@2021-01-06.yang'],
                         stdout=subprocess.PIPE, check=True)
    if res.returncode != 0:
        assert False, f'pyang failed: exit code {res.returncode}'
