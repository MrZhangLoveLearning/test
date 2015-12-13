# -*- coding: utf-8 -*-
"""Login in and parse the html """

import requests
from requests import Session
import re

def get_text(username):
    """Login
    Args: 
        username: the localtion of your building like 220706
                  the medicine school add Y like Y1101
                  the internation school add GJ  GJ1501
    Returns:
        the text of informations

    logining test

    >>> content = get_text('220706')
    >>> content != None
    True

    """
    session = Session()
    login_url = 'http://222.204.3.210/ssdf/Account/LogOn'
    response = session.post(login_url, data={'UserName':username})
    if response.ok:
        return response.content
    else:
        return None

READ_TIME = re.compile(
    ur'''
    # may be  have two read time 
    # one is the first time read 
    # the other is what we need ---the newest
    <td>\s*读数时间:\s*</td>  #  reading time 

    \s*   
         
    # the time formate 2015-12-12 12:00
    <td>(
        \d{4}   # the year
        -
        \d{1,2} # the month
        -
        \d{1,2} # the day
        \s
        \d{2}   # the hour
        :
        \d{2}   # the minute
        )\s*</td>

    ''',
    re.UNICODE | re.VERBOSE)

CURRENT_USED = re.compile(
    ur'''

    # current used the degree of electric
    # this month
    # one is the total
    # the other we need is used now

    <td>\s*本月度数\W度\W{2}\s*</td>
    \s*
    <td>
    # the degree of the electric
    (?P<degree>
    # the decimals of degree
    \d+      
    \.       
    \d+)      
    \s*
    </td>



    ''',
    re.UNICODE | re.VERBOSE)

BALANCE = re.compile(
    ur'''

    # current left the degree of electric
    # this month
        

    <td>\s*现金电量余额\W度\W{2}\s*</td>
    \s*
    <td>
    # the degree of the electric
    (?P<degree>
    # the decimals of degree
    \d+      
    \.       
    \d+)      
    \s*
    </td>



    ''',
    re.UNICODE | re.VERBOSE)


def parse_electric_info(content):
    """parse the informations

    Returns:
        a dict object
    >>> text = get_text('220706')
    >>> parse_electric_info(text)  # doctest: +ELLIPSIS
    {'balance': ..., 'currentUsed': ..., 'readTime': ...}

    """
    text = content.decode('utf-8')
    infos = {}
    read_list = READ_TIME.findall(text)
    read_times = len(read_list)
    infos['readTime'] = read_list[read_times-1]
    current_list = CURRENT_USED.findall(text)
    current_times = len(current_list)
    infos['currentUsed'] = current_list[current_times-1]
    infos['balance'] = BALANCE.findall(text)[0] 
    print infos
    return infos

if __name__ == '__main__':
    import doctest
    doctest.testmod()
