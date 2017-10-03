#!/usr/bin/env python
# coding=utf-8
"""Pattern matcher application"""

import os
import re
import logging
import collections

#patterns_dict = dict()
patterns_dict = collections.defaultdict(list)
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
        logging.debug("PATH ONLY ----- type_count=%d", type_count)
        parsed_path = parse_path(user_input)
        find_pattern_match(parsed_path)
    else:
        logging.debug("PATTERN ONLY ----- type_count=%d", type_count)
        parse_pattern(user_input)


def parse_path(path):
    parsed_path = parse(path)
    logging.debug("parsed path=%s", parsed_path)
    return parsed_path
    #paths.append(parsed_path)


def parse_pattern(pattern):
    parsed_pattern = parse(pattern)
    logging.debug("@@@@@@@@parsed pattern=%s", parsed_pattern)
    patterns.append(parsed_pattern)
    parsed_pattern_char_count = collections.Counter(parsed_pattern)
    wildcard_count = parsed_pattern_char_count.get("*")
    if wildcard_count == None:
        wildcard_count = 0
    logging.debug("wildcard_count=%d", wildcard_count)
    index = [pos for pos, char in enumerate(parsed_pattern) if char == "*"]
    logging.debug("storing key parsed_pattern=%s", parsed_pattern)
    logging.debug("storing value index=%s", index)
    patterns_dict[parsed_pattern].append(index)
    # for k,v in patterns_dict.items():
    #     for i in v:
    #         logging.debug("###############k=%s, i=%s", k, i)
    #TODO get freqcount of wildcards in pattern and store in dict
    #TODO store the indices of the wildcards in the dict


def parse(pattern):
    result = re.sub(",", "/", pattern)
    logging.debug("parse_pattern= %s", result)
    return result


def find_pattern_match(pattern):
    pattern_list = patterns_dict[pattern]
    logging.debug("patern_list= %s", pattern_list)


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
        logging.info("Start input processing...")
        while True:
            try:
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
            except EOFError as eof:
                logging.info("Reached the end of input.")
                break
        r = patterns_dict.get("w/x/*/*")
        logging.debug("!!!!!!result=%s", r)
        logging.debug("keys==%s", patterns_dict.keys())
    except ValueError as e:
        logging.error("An error has occurred, %s", e)
    except TypeError as te:
        logging.error("An error has occurred, %s", te)

if __name__ == "__main__":
    run()
