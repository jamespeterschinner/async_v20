1.0.1a1
=======
   Bug fixes:
      - Fixed code examples in bin directory

1.1.0a1
=======
   Bug fixes:
      - Model.series() returns data in more specific types instead of all 'str'
      - OandaClient methods now have correct signature instead of *args, **kwargs

1.1.1a1
=======
   Bug fixes:
      - Floating point numbers are rounded to the correct accuracy required for correct
      serialization.

1.1.2a1
=======
   Bug fixes:
      - OandaClient.initialize() method is now exposed
      - OandaClient is now also a context manager. To automatically close the http session

   Improvements:
      - Additional documentation

1.1.2a2
=======
   Improvements:
      - Additional documentation
1.1.2a3
=======
   Improvements:
      - Additional documentation

1.1.2a4
=======
   Improvements:
      - Additional documentation

1.1.2a4
=======
   Improvements:
      - Additional documentation

1.1.2a5
=======
   Improvements:
      - Added Travis CI
      - Added Codecov

1.1.3a0
=======
   Bug fixes:
      - Fixed incorrect annotation on Interface methods
      - Fixed argument passing bug caused by false'y evaluation

1.1.4a0
=======
   Bug fixes:
      - Fixed incorrect annotation on:
         - PUTPositionsInstrumentClose
         - GETPositionsInstrument

1.1.5a0
=======
   Bug fixes:
      - Issue method signatures were offset buy 1 argument due to handling of
      'self' parameter. Methods now displaying correct signature

1.1.5a1
=======
   Bug fixes:
        - Fix long description on PyPI
