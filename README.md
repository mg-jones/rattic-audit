rattic-audit
=======

## Description

The rattic-audit service exposes an API for auditing strengths of passwords stored in Rattic. Users or applications may query the service through HTTP and pass (optional) group parameters in the URL. For example:

- /			- (no parameters passed) Returns ALL password results.
- /all			- Returns ALL password results.
- /group/<groupname>	- Returns results for specified LDAP group (eg: sysops)

Results are returned in JSON.
