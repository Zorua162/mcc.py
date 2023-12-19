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
export latest_ver

pyproject_ver=$(grep version pyproject.toml | grep -Eo '".*"' | cut -d '"' -f 2)
echo "pyproject_ver $pyproject_ver"
echo "pyproject_ver=$pyproject_ver" >> "$GITHUB_ENV"

export GITHUB_ENV
