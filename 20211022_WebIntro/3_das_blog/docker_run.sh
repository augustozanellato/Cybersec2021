#!/bin/bash
docker run "$@" --rm -p "127.0.0.1:8084:80" --name "2018_das_blog" -it "2018_das_blog"
