https://overthewire.org/wargames/bandit

### SSH (13 -> 14)
`ssh -i [/path/to/private_key] user@address`
ssh usin 

### Netcat (14 -> 15)
`nc [ip-address] [port]`
miscellaneous TCP & UDP connections

### OpenSSL (15 -> 16)
`openssl s_client -connect [ip:port]`
test client for troubleshooting remote SSL/TLS connections

### Job Control (20 -> 21)
`bg`, `fg`, `jobs`, Ctrl+z

### Netcat (24 -> 25)
`nc [ip-address] [port] < file.txt`
sends contents of file.txt line by line to the listener

### /etc/passwd (25 -> 26)
this file stores user accounts info - user & group id, home directory, shell, etc

### more (25 -> 26, 26 -> 27)
1. activate *more* by reducing terminal window size
2. press 'v' when in the *more* pager to activate *vi* (unless VISUAL or EDITOR env var are defined)
3. run UNIX shell commands within *vi*
  * `:set shell=/bin/bash`
  * `:sh`

### git (28 -> 29, 30 -> 31)
`git log`
`git checkout [commit/ branch]`
`git branch -a`
`git show [blobs/trees/tags/commits]`

### Environment Variables (32 -> 33)
`$0` current script
`$SHELL` login shell
