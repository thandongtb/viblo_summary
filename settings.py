# -*- coding: utf-8 -*-

import logging
import os
# from http.cookiejar import CookieJar as cj

log = logging.getLogger(__name__)

PARENT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))

STOPWORDS_DIR = os.path.join(PARENT_DIRECTORY, 'resources/text')

# NLP stopwords are != regular stopwords for now...
NLP_STOPWORDS_VI = os.path.join(
    PARENT_DIRECTORY, 'resources/misc/stopwords-nlp-vi.txt')
