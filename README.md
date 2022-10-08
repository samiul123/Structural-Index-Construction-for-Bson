# Structural-Index-Construction-for-Bson

BSON is basically Binary JSON(Javascript Object Notation). It was designed for extreme levels of performance. It consists of the following characteristics.

- Lightweight
- Traversable
- Efficient

Here are some examples of JSON to BSON conversion.

```json
Json:
{
    "number": 5
}
Bson:
0x11 0x00 0x00 0x00                 // length (17) of the document in little-endian format
0x10                                // type (int32) of the value
0x6e 0x75 0x6d 0x62 0x65 0X72 0x00  // null terminated key (number)
0x05 0x00 0x00 0x00                 // value (5) in little-endian format
0x00                                // null terminator
```