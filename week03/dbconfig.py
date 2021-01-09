#!/usr/bin/env python
# -*- coding:utf-8 -*-
from configparser import ConfigParser


def read_db_config(filename='python_mysql_dev.ini', section='mysql'):
    """
    read database configuration file and return a dictionary object
    :param filename:
    :param section:
    :return:
    """

    # create parser and read ini configuration file
    parser = ConfigParser()
    parser.read(filename)

    if parser.has_section(section):
        items = parser.items(section)
    else:
        raise Exception('{0} not found in the {1} file'.format(section,filename))
    # print(items)
    return dict(items)


if __name__ == "__main__":
    print('aaa',read_db_config())