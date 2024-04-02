# test_group_data.py

import pytest
# Import the group_data function from your application code
from api.index import group_data

# Define test cases


def test_group_data_empty():
    # Test with empty data
    data = []
    grouped_data = group_data(data)
    assert grouped_data == {}


def test_group_data_single_group():
    # Test with a single group
    data = [
        ['7:00 AM', 'MW', 'APT2010', 'C',
            'SYSTEMS ANALYSIS & DESIGN', 'Mwangi, E', '35'],
        ['7:00 AM', 'MW', 'APT2011', 'D',
            'DATABASE MANAGEMENT SYSTEMS', 'Kamau, J', '30']
    ]
    grouped_data = group_data(data)
    expected_result = {
        '7:00 AM MW': [
            ['7:00 AM', 'MW', 'APT2010', 'C',
                'SYSTEMS ANALYSIS & DESIGN', 'Mwangi, E', '35'],
            ['7:00 AM', 'MW', 'APT2011', 'D',
             'DATABASE MANAGEMENT SYSTEMS', 'Kamau, J', '30']
        ]
    }
    assert grouped_data == expected_result


def test_group_data_multiple_groups():
    # Test with multiple groups
    data = [
        ['7:00 AM', 'MW', 'APT2010', 'C',
            'SYSTEMS ANALYSIS & DESIGN', 'Mwangi, E', '35'],
        ['7:00 AM', 'TH', 'APT2012', 'A', 'SOFTWARE ENGINEERING', 'Wanjiru, F', '25'],
        ['8:00 AM', 'MW', 'APT2011', 'D',
            'DATABASE MANAGEMENT SYSTEMS', 'Kamau, J', '30'],
        ['8:00 AM', 'TH', 'APT2013', 'B', 'WEB DEVELOPMENT', 'Ochieng, S', '20']
    ]
    grouped_data = group_data(data)
    expected_result = {
        '7:00 AM MW': [
            ['7:00 AM', 'MW', 'APT2010', 'C',
                'SYSTEMS ANALYSIS & DESIGN', 'Mwangi, E', '35']
        ],
        '7:00 AM TH': [
            ['7:00 AM', 'TH', 'APT2012', 'A',
                'SOFTWARE ENGINEERING', 'Wanjiru, F', '25']
        ],
        '8:00 AM MW': [
            ['8:00 AM', 'MW', 'APT2011', 'D',
                'DATABASE MANAGEMENT SYSTEMS', 'Kamau, J', '30']
        ],
        '8:00 AM TH': [
            ['8:00 AM', 'TH', 'APT2013', 'B', 'WEB DEVELOPMENT', 'Ochieng, S', '20']
        ]
    }
    assert grouped_data == expected_result
