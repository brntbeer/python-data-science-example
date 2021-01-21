#!/usr/bin/env python3

import sys
import traceback
import urllib.error
import urllib.request

#
# NOTE: Accessing the URL below too frequently will likely cause the server to
#       start rejecting your requests.
#
try:
    with urllib.request.urlopen("https://api.github.com/octocat") as response:
        html = response.read().decode("utf8")
        print(html)
except urllib.error.HTTPError as error:
    sys.stderr.write(
        "Error: server returned status code {0} ({1}).\n".format(
            error.code, error.reason
        )
    )
except Exception as error:
    sys.stderr.write(traceback.format_exc() + "\n")