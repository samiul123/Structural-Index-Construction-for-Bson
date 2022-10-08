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
```json
Json: 
{
    "bool": true,
    "string": "json"
}
Bson:
0x1d 0x00 0x00 0x00                 // length (29) of the document in little-endian format
0x08                                // type (boolean) of the value
0x62 0x6f 0x6f 0x6c 0x00            // null terminated key (bool)
0x01                                // value (true)
0x02                                // type (string)
0x73 0x74 0x72 0x69 0x6e 0x67 0x00  // null terminated key (string)
0x05 0x00 0x00 0x00                 // length of the null-terminated string value (4+1=5) in little-endian format
0x6a 0x73 0x6f 0x6e 0x00            // null terminated string value (json)
0x00                                // null terminator
```
```json
Json:
{
    "array": [1, 2, 3]
}
This object will be considered as
{
    "array": {
        "0": 1,
        "1": 2,
        "2": 3
    }
}
where the nested keys are considered as the index of the original array
Bson:
0x26 0x00 0x00 0x00                 // length (38)
0x04                                // type (array)
0x61 0x72 0x72 0x61 0x79 0x00       // null-terminated key (array)
0x1a 0x00 0x00 0x00                 // length (26)
0x10 0x30 0x00 0x01 0x00 0x00 0x00  // type (int32) null-terminated key (0) value (1)
0x10 0x31 0x00 0x02 0x00 0x00 0x00  // type (int32) null-terminated key (1) value (2)
0x10 0x32 0x00 0x03 0x00 0x00 0x00  // type (int32) null-terminated key (2) value (3)
0x00                                // null terminator of inner object
0x00                                // null terminator of outer object
```