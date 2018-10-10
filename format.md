# Formats

There are (currently, apparently) four formats:

* 220 column minor planet
* 90 column minor planet
* 256 column comet
* 220 column natural satellite format

Partial documention relevant to the 220 column format was obtained by email
query:

```
Boardman, Ian <ian.boardman@cfa.harvard.edu>
11/7/16

to Gareth, Sonia 
Hi. Can you send me the syntax / format of the *.var files in cgi-data/neocp/var ?
Thanks.
```

```
Williams, Gareth <gwilliams@cfa.harvard.edu>
11/7/16

to Ian, Sonia 
  Cols      Format   Use
  1-  5      A5      Permanent designation (packed form)
or
  1-  7      A7      Provisional designation (packed form)

  8- 12     F5.2     Slope parameter, G
 13- 24     A12      Date of perihelion passage/JDT (packed form)
 25- 34     F10.7    Argument of perihelion (deg/J2000.0)
 35- 44     F10.7    Longitude of ascending node (deg/J2000.0)
 45- 54     F10.7    Inclination of orbit (deg/J2000.0)
 55- 64     F10.9    Perihelion distance (AU)
 65- 74     F10.9    Eccentricity
 81- 90     A10      Designation (unpacked form)
 92- 95     F4.1     Absolute magnitude, H
 96-140   Low-precision "readable" elements
142-144     I3       Number of oppositions included in solution
146-150     I5       Arc length of observations included in solution (/days)
152-156     I5       Number of observations included in solution
160-168     A9       Computer name
170-178     A9       Reference
180-184     A5       Date of first included observation (packed form)
186-190     A5       Date of last included observation (packed form)
192-196     F5.2     r.m.s. fit of included obserations (/")

  Stuff beyond col 196 can be ignored.

  Packed formats are described in the Documentation link on the website.

  Values in cols 25-74 are normally stored without the dp, the stated
Fortran format specifiers will read the values correctly, even for
perihelion distances >= 10 AU, where an explicit dp is included.
```

Also Gareth suggests reading source code at
bitbucket.org/mpcdev/mpclib/convert.py and
bitbucket.org/mpcdev/onetime_converters/convert_orbits.py.
