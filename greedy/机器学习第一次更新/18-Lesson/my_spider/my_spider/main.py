__author__ = "zhou"
__date__ = "2019-06-04 20:47"

from scrapy.cmdline import execute
import sys
import os


sys.path.append(os.path.dirname(os.path.abspath(__file__)))
execute(["scrapy", "crawl", "tieba"])

