check:
    /usr/bin/grep -F -x -- ready src/payload.txt
    /usr/bin/grep -F -x -- required src/guard.txt
    /usr/bin/python3.13 -I -S -B scripts/check_audit.py
