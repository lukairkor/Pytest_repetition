#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 20:10:14 2021

@author: lukas
"""
import pytest

# content of test_sample.py
def inc(x):
    return x + 1

def test_answer():
    assert inc(3) == 5
    
def test_list():
    assert 1 in [2, 3, 4]
    
def test_if_less():
    a = 2
    b = 5
    assert a < b
@pytest.mark.this_one  
def test_find():
    assert 'fizz' not in 'fizzbuzz'