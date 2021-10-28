#!/bin/bash
docker run "$@" --rm -p "127.0.0.1:8083:80" --name "ajax_not_borax" -it "zenhackteam/ajax_not_borax"
