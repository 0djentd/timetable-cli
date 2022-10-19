#!/usr/bin/env bash

echo "# timetable-cli" > README.md
echo "## Installation" >> README.md
echo '```' >> README.md
echo "pip install timetable-cli" >> README.md
echo '```' >> README.md
echo "## How to use" >> README.md
echo '```' >> README.md
poetry run timetable-cli --help >> README.md
echo '```' >> README.md
