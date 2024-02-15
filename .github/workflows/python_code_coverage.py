name: Deploy

on:
  push:
    branches:
      - main

jobs:
  my_job:
    runs-on: ubuntu-18.04

    steps:
      - name: Python Coverage
        # You may pin to the exact commit or the version.
        # uses: orgoro/coverage@4e3bc9302f715595336a40f7dd4a3b15c687bdb4
        uses: orgoro/coverage@v3.1
        with:
          # Local path to a coverage xml file like the output of pytest --cov
          coverageFile: ${{ secrets.COVERAGE_FILE }}
          # GitHub token
          token: ${{ secrets.GITHUB_TOKEN }}
          # The coverage threshold for average over all files [0,1]
          thresholdAll: # optional, default is 0.0
          # The coverage threshold for average over new files [0,1]
          thresholdNew: # optional, default is 0.0
          # The coverage threshold for average over modified files [0,1]
          thresholdModified: # optional, default is 0.0
          
