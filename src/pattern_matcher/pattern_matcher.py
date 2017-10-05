#!/usr/bin/env python
# coding=utf-8
"""Pattern matcher application"""

import os
import re
import logging
import collections

patterns_dict = collections.defaultdict(list)
pattern_length_dict = collections.defaultdict(list)
patterns = list()
paths = list()
NO_MATCH = "NO MATCH"


def logger_config():
    logging.basicConfig(level=logging.INFO, format=("[###%(levelname)s] "
                                                    "%(asctime)s: "
                                                    "%(filename)s: "
                                                    "%(funcName)s(): "
                                                    "%(lineno)d: "
                                                    "%(message)s\n"))


def process_input(user_input, type_count):
    if type_count % 2 == 0:
        logging.debug("PATH ONLY ----- type_count=%d", type_count)
        process_pattern_match(user_input)
    else:
        logging.debug("PATTERN ONLY ----- type_count=%d", type_count)
        parsed_input = parse(user_input)
        parse_pattern(parsed_input)


def parse_pattern(parsed_pattern):
    logging.debug("parsed pattern=%s", parsed_pattern)
    patterns.append(parsed_pattern)
    set_wildcards_indices_from_pattern(parsed_pattern)
    set_slashes_indices_from_pattern(parsed_pattern)


def set_wildcards_indices_from_pattern(parsed_pattern):
    index = [pos for pos, char in enumerate(parsed_pattern) if char == "*"]
    patterns_dict[parsed_pattern].append(index)


def set_slashes_indices_from_pattern(parsed_pattern):
    slash_count = [pos for pos, char in enumerate(parsed_pattern) if char == "/"]
    pattern_length_dict[len(slash_count)].append(parsed_pattern)


def get_slashes_indices_from_strip_path(strip_path):
    slash_count = [pos for pos, char in enumerate(strip_path) if char == "/"]
    print slash_count
    return pattern_length_dict[len(slash_count)]


def parse(pattern):
    logging.debug("Sub / for , in %s", pattern)
    return re.sub(",", "/", pattern)


def process_pattern_match(path):
    logging.debug("Processing %s to find pattern match.", path)
    strip_path = path.strip("/")
    logging.debug("strip path: %s, path: %s", strip_path, path)
    path_list = list(strip_path)
    print path_list
    possible_patterns = get_slashes_indices_from_strip_path(strip_path)
    print possible_patterns
    results_list = list()
    result = NO_MATCH

    if len(possible_patterns) == 0:
        result = NO_MATCH
    else:
        for pattern in possible_patterns:
            pattern_list = list(pattern)
            wildcards = patterns_dict.get(pattern)
            if wildcards is None:
                wildcards = 0
            else:
                wildcards = wildcards[0]
            logging.debug("Pattern wildcard indices= %s", wildcards)
            if not wildcards:
                logging.debug("An empty wildcards list - test the pattern")
                if pattern == strip_path:
                    results_list.append(pattern)
                    break
            for index in wildcards:
                pattern_list[index] = path_list[index]
            result = "".join(pattern_list)
            if result == strip_path:
                logging.debug("Adding pattern %s to list of results that"
                              " could match the path %s.", pattern, path)
                results_list.append(pattern)
    if len(results_list) == 0:
        logging.debug("Result list is empty.")
        result = NO_MATCH
    elif len(results_list) == 1:
        result = results_list[0]
        logging.debug("Result has one result %s.", result)
    else:
        maxvalue = 0
        maxpattern = ""
        for i in results_list:
            wildcards = patterns_dict.get(i)
            maxvalue_tmp = sum(wildcards[0])
            if maxvalue_tmp == 0 and pattern == path:
                result = pattern
                break
            if len(wildcards[0]) == 1:
                maxpattern = i
                break
            logging.debug("Pattern sum the number of wildcards= %d", maxvalue_tmp)
            if maxvalue_tmp > maxvalue:
                maxpattern = i
                maxvalue = maxvalue_tmp
        result = maxpattern
    print re.sub("/", ",", result)


def run():
    logger_config()
    lines_count = 0
    type_count = 0
    try:
        logging.debug("Start input processing...")
        while True:
            try:
                user_input = raw_input()
                if not user_input:
                    logging.debug("No user input")
                    break
                if user_input.isdigit():
                    logging.debug("User input is an int")
                    type_count = type_count + 1
                    continue
                if not user_input.isdigit():
                    logging.debug("User input is a pattern or path")
                    logging.debug("user_input=%s", user_input)
                    process_input(user_input, type_count)
                    continue
            except EOFError as eof:
                logging.debug("Reached the end of input.")
                break
    except ValueError as e:
        logging.error("An error has occurred, %s", e)
    except TypeError as te:
        logging.error("An error has occurred, %s", te)

if __name__ == "__main__":
    run()
