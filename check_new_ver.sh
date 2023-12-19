#!/bin/bash
set -e
set -x
echo "Get latest test package version"
echo "$1"
latest_package=$(curl "$1" | sed 's/<[^>]*>//g' | tail -n 3 | head -n 1)
echo "Extract the version"
latest_ver=$(echo "$latest_package" | sed 's/mcc.py-//g' | sed 's/.tar.gz//g')
echo "latest_ver $latest_ver"
echo "latest_ver=$latest_ver" >> "$GITHUB_ENV"

pyproject_ver=$(grep version pyproject.toml | grep -Eo '".*"' | cut -d '"' -f 2)
echo "pyproject_version $pyproject_ver"
echo "pyproject_version=$pyproject_ver" >> "$GITHUB_ENV"
