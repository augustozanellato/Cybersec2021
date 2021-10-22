#!/bin/bash
docker run "$@" --rm -p "127.0.0.1:8085:80" --name "ajax_not_soap" -it "spritzers/ajax_not_soap"
