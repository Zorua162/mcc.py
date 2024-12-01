#!/bin/bash
set -e
set -x
echo "Get latest test package version"
latest_package=$(curl https://test.pypi.org/simple/mcc-py/ \
                | sed 's/<[^>]*>//g' | tail -n 3 | head -n 1)
echo "Extract the version"
latest_ver=$(echo "$latest_package" | sed 's/mcc.py-//g' | sed 's/.tar.gz//g')
pre_ver=$(echo "$latest_ver" | sed -E 's/[0-9]+.[0-9]+.[0-9]+//g')
if [[ "$pre_ver" == "" ]]; then
    dev_ver="$latest_ver"-pre1
else
    prev_pre_ver=${pre_ver/-pre/}
    next_ver=$((prev_pre_ver+1))
    dev_ver=$latest_ver-pre$next_ver
fi


# No-longer used, as this would need to be done before the "build" stage, which
# means that the build stage would need to be run once for each location.
echo "$dev_ver"

# sed -i -E 's/version = "(.*?)"/version = "'"$dev_ver"'"/g' pyproject.toml
