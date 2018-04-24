``dscl`` stands for directory services command line interface.

One thing it can be used for is to set up a new user.

#### Set up a new user

The following requires ``sudo`` (or ``root``). 

To set up a new user ``u``:

```
dscl . -create /Users/u
dscl . -create /Users/u UserShell /bin/bash
dscl . -create /Users/u RealName "John Smith"
dscl . -create /Users/u UniqueID 1001"
dscl . -create /Users/u PrimaryGroupID 1000"
dscl . -create /Users/u NFSHomeDirectory /Local/Users/u
dscl . -passwd /Users/u password
dscl . -append /Groups/admin GroupMembership u
```

To upgrade a user from Standard to Admin, only the last is required.