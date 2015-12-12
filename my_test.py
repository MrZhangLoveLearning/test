# -*- coding:utf-8 -*-
import re
def test_patterns(text, patterns=[]):
    for pattern in patterns:
        print 'Pattern %r \n' % (pattern)
        print '%r' % text
        for match in re.finditer(pattern, text):
            s = match.start()
            e = match.end()
            substr = text[s:e]
            n_backslashes = text[:s].count('\\')
            prefix = '.' * (s + n_backslashes)
            print '%s%r' % (prefix, substr)
            print match.groups()
            if match.groupdict():
                print '%s%s' % (' '*(len(text)-s), match.groupdict())
        print 
    return

ADDRESS = re.compile(
    r'''
    ^
    
    # A name is made of letters, and may include "."

    (?P<name>([\w.]+\s+)*[\w.]+


        )?
        
        
    
    # if have name then need <*>
    (?(name)

        # there is a name
        (?P<brackets>(?=<.*>$))
        |
        (?=([^<].*[^>]$))

        )

    # An address: username@domain.tld
    
    # Ignore noreply address 
    (?!noreply@.*$)
    (?(brackets)<|\s*)

    (?P<username>[\w\d.+-]+) # username
    # (?<!noreply)
    (@)
    ([\w\d.]+\.)+  # domain
    (com|org|edu)   # TODO:support more top-level domains
    (?(brackets)>|\s*)
    ''',
    re.UNICODE | re.VERBOSE)
TWIT = re.compile(
    '''
    # A twitter handle:@username
    (?<=@)
    ([\w\d_]+) # username 

    ''',
    re.UNICODE | re.VERBOSE)

    

PATTERN = '''


    ([\w\d.+-]+) # username
    (@)
    ([\w\d.]+\.)+  # domain
    (com|org|edu)   # TODO:support more top-level domains
    '''