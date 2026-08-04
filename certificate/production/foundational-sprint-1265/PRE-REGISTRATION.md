# Pre-registration: one prefix for all four coordinates

Independent source and output grids are not sufficient for the operator
response triangle, which compares both through one numerical output prefix.
Register the corrected target.

For one width `w`, average a **single** shifted grid applied simultaneously to

```text
y, u, A=a(y), B=-u.
```

Some shift must retain a positive submeasure on which both pairs share cells,
with total loss at most

```text
[integral |y-u| + integral |A-B|]/w.
```

Every prefix of the retained grid must then have identical Alice/Bob
indicators before and after response.  No independent reindexing is allowed.

