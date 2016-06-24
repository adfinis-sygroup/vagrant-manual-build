#!/usr/bin/env bash
C=''
for i in "$@"; do
	C="$C \"${i//\"/\\\"}\""
done

cat Vagrantfile  | grep define | grep -v -E "\s*#" | cut -d '"' -f 2 |
	xargs -I% vagrant ssh % -c "/vagrant/build.py % $C"

