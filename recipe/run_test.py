import platform, sys

if platform.python_version_tuple() < ('3', '7', '0'):
    from pysnmp.entity.rfc3413.oneliner import cmdgen
else:
    print("WARNING :: Skipping tests due to asyncio.async() being a syntax error on Python >=3.7.0, pysnmp.asyncio does not work on 3.7 and above")
    sys.exit(0)
