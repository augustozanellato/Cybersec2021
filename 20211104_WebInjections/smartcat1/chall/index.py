#!/usr/bin/env python

import cgi
import os
import subprocess


def application(environ, start_response):
    header_xpb = [
        "mod_cassette_is_back/0.1",
        "format-me-i-im-famous",
        "dirbuster.will.not.help.you",
        "solve_me_already",
    ]
    headers = [("X-Powered-By", header_xpb[os.getpid() % 4]), ("Content-type", "text/html")]

    try:
        request_body_size = int(environ.get("CONTENT_LENGTH", 0))
    except (ValueError):
        request_body_size = 0

    request_body = environ["wsgi.input"].read(request_body_size)
    d = cgi.parse_qs(request_body)
    dest = d.get("dest", [""])[0]

    r = """
    <html>

    <head><title>Can I haz Smart Cat ???</title></head>

    <body>

      <h3> Smart Cat debugging interface </h3>
    """

    blacklist = " $;&|({`\t"
    results = ""

    if dest:
        for badchar in blacklist:
            if badchar in dest:
                results = "Bad character %s in dest" % badchar
                break

        if "%n" in dest:
            results = "Segmentation fault"

        if not results:
            try:
                results = subprocess.check_output("ping -c 1 " + dest, shell=True)
            except:
                results = "Error running " + "ping -c 1 " + dest

    r += """

      <form method="post" action="index.cgi">
        <p>Ping destination: <input type="text" name="dest"/></p>
      </form>

      <p>Ping results:</p><br/>
      <pre>%s</pre>

    </body>

    </html>
    """ % cgi.escape(
        results
    )
    status = "200 OK"
    start_response(status, headers)
    return iter([r])
