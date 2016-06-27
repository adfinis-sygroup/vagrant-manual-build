#!/usr/bin/env bash
set -e
C=''
for i in "$@"; do
	C="$C \"${i//\"/\\\"}\""
done

cat Vagrantfile  | grep define | grep -v -E "\s*#" | cut -d '"' -f 2 |
	xargs -I% bash -c "vagrant up % && vagrant ssh % -c \"/vagrant/build.py % $C\" && vagrant halt %"

