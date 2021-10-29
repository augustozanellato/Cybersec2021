#!/usr/bin/python3
import subprocess

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/source")
def sourcecode():
    return render_template("./static/source.py")


@app.route("/flag")
def get():
    if request.method == "GET":
        ip = request.args.get("ip")
        port = request.args.get("port")
        flag = open("flag.txt").readline()
        allowed = {"allowed_ip": "8.8.8.8", "allowed_port": port, "allowed_flag": flag}
        if ip and ip != "" and port and port != "":
            if port.isdigit():
                if ip == allowed.get("allowed_ip"):
                    subprocess.Popen(
                        "cat flag.txt > /dev/tcp/" + str(ip) + "/" + str(port), shell=True, executable="bash"
                    )
                    return ("SUCCESS: The flag have been sent to DST IP %s and  DST PORT %s\n") % (ip, port)
                else:
                    return ("You have choose IP " + ip + ", but only %(allowed_ip)s will receive the key\n") % allowed
            else:
                return "Port invalid\n"
        else:
            return "Please choose an IP and a PORT\n"
    else:
        return ("FAIL: Method HTTP not allowed (%s)\n") % (request.method)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
