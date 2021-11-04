#!/bin/bash
docker run "$@" --rm -p "127.0.0.1:124:80" --name "saltfish" -it "zenhackteam/saltfish"
