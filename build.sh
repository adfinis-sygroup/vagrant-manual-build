#!/usr/bin/env bash
set -e
C=''
for i in "$@"; do
	C="$C \"${i//\"/\\\"}\""
done

for distro in `cat Vagrantfile  | grep define | grep -v -E "\s*#" | cut -d '"' -f 2`; do
    vagrant up $distro && \
        vagrant ssh $distro -c "/vagrant/build.py $distro $C" && \
        vagrant halt $distro || \
        exit 1
done
echo All packages successfully built!
