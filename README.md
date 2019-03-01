Based off https://github.com/BlackrockDigital/startbootstrap-agency, with a good portion of adjustments (jekyll and bibtex support) adapted from https://github.com/rabernat/rabernat.github.io.

Build locally using `rake generate & jekyll serve`, remotely using `rake publish`. This builds the page locally, creates a temporary local git repo and then pushes that to remote. Hence directly `git push`ing will make the page build fail.
