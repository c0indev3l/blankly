#!/bin/bash

set -e

export DEBIAN_FRONTEND=noninteractive
declare -A APTOPTS
APTOPTS[1]="--assume-yes"
APTOPTS[2]="--no-install-recommends"

echo Updating Repositories
apt-get update

echo Installing base dependencies...
apt-get install ${APTOPTS[*]} python3-pytest
echo

echo Clean up downloaded resources in order to free space
apt-get clean
echo
