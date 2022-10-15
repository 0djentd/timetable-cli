#!/usr/bin/env bash

echo "# timetable-cli" > README.md
echo "## How to use" >> README.md
echo '```' >> README.md
poetry run timetable-cli --help >> README.md
echo '```' >> README.md
echo '```' >> README.md
poetry run timetable-cli "show" --help >> README.md
echo '```' >> README.md
echo '```' >> README.md
poetry run timetable-cli "watch" --help >> README.md
echo '```' >> README.md
echo '```' >> README.md
poetry run timetable-cli "status" --help >> README.md
echo '```' >> README.md
