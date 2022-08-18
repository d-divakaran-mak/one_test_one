# -*- coding: utf-8 -*-

# Checking Git tags

def get_bugs():
    return ['bug2-v1', 'bug3-v2', 'bug4-v2', 'bug5-v1', 'bug6-v3', 'bug7-v1',
            'bug8-v2', 'bug9-v1', 'bug10-v1']


def get_features():
    return ['feature1', 'feature2']


def get_version():
    return '1.0.0'


if __name__ == '__main__':
    if get_bugs():
        print "Bugs : %s" % ', '.join(get_bugs())
    if get_features():
        print "Features : %s" % ', '.join(get_features())
    print "Version : %s" % get_version()
