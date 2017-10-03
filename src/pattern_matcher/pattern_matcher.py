#!/usr/bin/env python
# coding=utf-8
"""Pattern matcher application"""

import os
import re
import logging

patterns_dict = dict()
patterns = list()
paths = list()


def logger_config():
    logging.basicConfig(level=logging.DEBUG, format=("[###%(levelname)s] "
                                                    "%(asctime)s: "
                                                    "%(filename)s: "
                                                    "%(funcName)s(): "
                                                    "%(lineno)d: "
                                                    "%(message)s\n"))

def process_input(user_input, lines_count, type_count):
    if type_count % 2 == 0:
        parse_path(user_input)
    else:
        parse_pattern(user_input)


def parse_path(path):
    parsed_path = parse(path)
    logging.debug("parsed path=%s", parsed_path)
    paths.append(parsed_path)


def parse_pattern(pattern):
    parsed_pattern = parse(pattern)
    logging.debug("parsed path=%s", parsed_pattern)
    patterns.append(parsed_pattern)
    #TODO get freqcount of wildcards in pattern and store in dict
    #TODO store the indices of the wildcards in the dict


def parse(pattern):
    result = re.sub(",", "/", pattern)
    logging.debug("parse_pattern= %s", result)
    return result


def add_patterns_dict(pattern):
    #TODO
    print "adding them"


def find_pattern_matches():
    #TODO
    print "yes"


def pattern_match_path(path, pattern):
    logging.debug("path= %s, pattern= %s", path, pattern)
    if len(path) is not len(pattern):
        print "NO MATCH"
    elif path != pattern:
        print "NO MATCH"
    else:
        print pattern


def run():
    logger_config()
    lines_count = 0
    type_count = 0
    try:
        logging.info("Starting")
        while True:
            user_input = raw_input()
            if not user_input:
                break
            if user_input.isdigit():
                lines_count = int(user_input)
                type_count = type_count + 1
                logging.debug("lines_count=%d, type_count=%d", lines_count, type_count)
                continue
            if not user_input.isdigit():
                logging.debug("user_input=%s", user_input)
                process_input(user_input, lines_count, type_count)
                continue
        find_pattern_matches()
    except ValueError as e:
        logging.error("An error has occurred, %s", e)
    except TypeError as te:
        logging.error("An error has occurred, %s", te)

if __name__ == "__main__":
    run()
