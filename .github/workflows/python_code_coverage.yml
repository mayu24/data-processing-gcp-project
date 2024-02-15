name: Python Coverage

on:
  push:
    branches:
      - master

jobs:
  my_job:
    runs-on: ubuntu-18.04

    steps:
      - name: Python Coverage
        uses: orgoro/coverage@v3.1
        with:
          coverageFile: ${{ secrets.COVERAGE_FILE }}
          token: ${{ secrets.GITHUB_TOKEN }}
          thresholdAll: 0.0
          thresholdNew: 0.0
          thresholdModified: 0.0

      - name: Upload coverage report
        uses: actions/upload-artifact@v2
        with:
          name: coverage-report
          path: ${{ secrets.COVERAGE_FILE }}

      - name: Comment on pull request with coverage report
        uses: unsplash/comment-on-pr@v1
        with:
          msg: |
            Coverage Report:
            ![Coverage Report](https://github.com/${{ github.repository }}/raw/main/${{ secrets.COVERAGE_FILE }})
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
