#### The problem

Some applications installed by Homebrew are not signed, including ``gdb``.

I found instructions for how to self-sign code for macOS [here](https://sourceware.org/gdb/wiki/PermissionsDarwin) and the [error msg here](https://sourceware.org/gdb/wiki/BuildingOnDarwin).

#### signing

- Start Keychain Access application (``/Applications/Utilities/Keychain Access.app``)
- Open the menu item ``/Keychain Access/Certificate Assistant/Create a Certificate...``
- Choose a name (``gdb-cert`` in the example)
- set ``Identity Type`` to ``Self Signed Root``
- set ``Certificate Type`` to ``Code Signing``
- select the ``Let me override defaults``

Click several times on Continue until you get to the ``Specify a Location For The Certificate`` screen,

- then set ``Keychain`` to ``System``
- Finally, quit the Keychain Access application 

to refresh the certificate store.

#### Trust the certificate

Create

*gdb-entitlement.xml*

```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>com.apple.security.cs.debugger</key>
    <true/>
</dict>
</plist>
</pre>
```

- ``codesign --entitlements gdb-entitlement.xml -fs gdb-cert $(which gdb)``

To check:

```
> codesign -vv $(which gdb)
> codesign -d --entitlements - $(which gdb)
```

Reboot to update ``taskgated``.

If you have problems look at the logs

```
log stream --predicate 'process = "taskgated" OR (process = "kernel" AND eventMessage CONTAINS "macOSTaskPolicy")' --info
```

#### Finally

On 10.12 (Sierra) or later with SIP, you need to run this:
```
  echo "set startup-with-shell off" >> ~/.gdbinit
```