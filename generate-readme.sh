#!/bin/bash

echo "# timetable-cli" > README.md
echo "## How to use" >> README.md
echo '```' >> README.md
poetry run timetable-cli --help >> README.md
echo '```' >> README.md
