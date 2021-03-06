#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Parse term query before passing it to the PhiloLogic4 library."""

import re

def parse_query(query_terms, config):
    """Parse query function."""
    for pattern, replacement in config.query_parser_regex:
        query_terms = re.sub(r"{}".format(pattern), replacement, query_terms, re.U)
    return query_terms
