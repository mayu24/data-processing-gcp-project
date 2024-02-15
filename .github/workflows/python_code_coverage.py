- name: Python Coverage
  # You may pin to the exact commit or the version.
  # uses: orgoro/coverage@4e3bc9302f715595336a40f7dd4a3b15c687bdb4
  uses: orgoro/coverage@v3.1
  with:
    # local path to a covergae xml file like the output of pytest --cov
    coverageFile: 
    # github token
    token: 
    # the coverage threshold for average over all files [0,1]
    thresholdAll: # optional, default is 0.0
    # the coverage threshold for average over new files [0,1]
    thresholdNew: # optional, default is 0.0
    # the coverage threshold for average over new files [0,1]
    thresholdModified: # optional, default is 0.0
          
