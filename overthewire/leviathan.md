https://overthewire.org/wargames/leviathan/

### Binary Analysis (1 -> 2, 2 -> 3)
https://opensource.com/article/20/4/linux-binary-analysis
- **ldd**: print shared libraries dependencies (may execute)
- **ltrace**: library call tracer
- **objdump** 
- **readelf**
- **strace**

### Special Character Escaping (2 -> 3)
Access checking may be separate from access using. If separate files are checked and used, consider symlink with problematic names (arising from buggy character escaping).

Alternative Solution: [TOCTOU](https://en.wikipedia.org/wiki/Time-of-check_to_time-of-use)


1. access() checks permissions based on process' real UID (not effective UID)
2. ltrace runs are useful, but will mask the EUID of the process of interest
