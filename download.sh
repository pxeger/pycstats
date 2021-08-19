#!/usr/bin/env bash
set -e
rm -rf venv packages
mkdir packages
python -m venv venv
source venv/bin/activate
N=100
J=12
curl -L 'https://github.com/hugovk/top-pypi-packages/raw/2021.04/top-pypi-packages-365-days.min.json' \
    | jq -r '.rows[] | .project' \
    | head -n $N \
    | nl \
    | while read -r i package; do
        while [ $(jobs -r | wc -l) -gt $J ]; do
            sleep 1
        done
        echo "($i/$N) $package"
        ( pip download --no-deps -d packages/$package $package
          cd packages/$package
          ls | while read -r file; do
              unzip $file || tar -xf $file
          done
          python -m compileall .
        ) > packages/$package.1.log 2> packages/$package.2.log &
    done

wait -f
echo Done!
