#!/usr/bin/env bash

cat Vagrantfile  | grep define | cut -d '"' -f 2 | xargs -I% vagrant ssh % -c "/vagrant/build.py %"

