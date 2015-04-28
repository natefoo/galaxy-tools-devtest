# galaxy-tools-devtest

Galaxy tools useful for performing development and admin tasks typically
related to job control or Galaxy server administration. These can be useful for
things like testing walltime limits, job resubmission, memory limits, etc.

## tools

- Copy: Copy input file to output file
- Echo: Echo input field to output file
- Malloc: Allocate/hold some amount of memory
- Uname: Execute `uname -a`

All tools incorporate a "sleep" value in seconds that is executed prior to the
tool's primary operation.
