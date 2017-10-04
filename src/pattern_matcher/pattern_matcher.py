#!/usr/bin/env python
# coding=utf-8
"""Pattern matcher application"""

import os
import re
import logging
import collections

patterns_dict = collections.defaultdict(list) #wildcard indices
pattern_length_dict = collections.defaultdict(list)
patterns = list()
paths = list()
NO_MATCH = "NO MATCH"

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
    logging.debug("parsed pattern=%s", parsed_pattern)
    patterns.append(parsed_pattern)
    parsed_pattern_char_count = collections.Counter(parsed_pattern)
    wildcard_count = parsed_pattern_char_count.get("*")
    if wildcard_count == None:
        wildcard_count = 0
    logging.debug("wildcard_count=%d", wildcard_count)
    slash_count = [pos for pos, char in enumerate(parsed_pattern) if char == "/"]
    pattern_length_dict[len(slash_count)].append(parsed_pattern)
    index = [pos for pos, char in enumerate(parsed_pattern) if char == "*"]
    patterns_dict[parsed_pattern].append(index)


def parse(pattern):
    result = re.sub(",", "/", pattern)
    logging.debug("parse_pattern= %s", result)
    return result


def find_pattern_match(pattern):
    logging.debug("PATTERN ==== %s", pattern)
#    pattern_list = patterns_dict[pattern]
#    logging.debug("patern_list= %s", pattern_list)


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

        path = "a/b/c/"
        path_list = list(path)
        slash_count = [pos for pos, char in enumerate(path) if char == "/"]
        # r = patterns_dict.get(pattern)
        # wildcards = 0
        # if r is not None:
        #     wildcards = r[0]
        possible_patterns = pattern_length_dict[len(slash_count)]
        if len(possible_patterns) == 0:
            result = NO_MATCH
        else:
            for pattern in possible_patterns:
                pattern_list = list(pattern)
                wildcards = patterns_dict.get(pattern)[0]
                for index in wildcards:
                    pattern_list[index] = path_list[index]
                result = "".join(pattern_list)
                print result

        #pattern_str_list = list(pattern)
        logging.debug("RESULT====%s", result)

        logging.debug("wildcards dict")
        for k, v in patterns_dict.iteritems():
            print k, v

        logging.debug("legnth dict")
        for k, v in pattern_length_dict.iteritems():
            print k, v
    except ValueError as e:
        logging.error("An error has occurred, %s", e)
    except TypeError as te:
        logging.error("An error has occurred, %s", te)

if __name__ == "__main__":
    run()
