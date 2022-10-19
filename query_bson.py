def query(query_str, file_name):
    with open(file_name, 'rb') as f:
        data = f.read()

    query_list = query_str.split(".")
    pointer = 1
    result = ""

    def query_helper(start=0, pointer=1):
        nonlocal result

        doc_length = int.from_bytes(data[start:start+4], byteorder="little")
        end = start + doc_length
        start += 4
        while start < end:
            type = int.from_bytes(data[start:start+1], byteorder="big")
            if type == 0:
                start += 1
                continue

            start += 1
            key_s = start
            while int(data[key_s]) != 0:
                key_s += 1
            key = data[start:key_s].decode()
            start = key_s+1

            if type == 2:
                value_length = int.from_bytes(data[start:start+4], byteorder="little")
                if key == query_list[pointer]:
                    start += 4
                    result = data[start:start+value_length-1].decode()
                    start += value_length+1
                else:
                    start += value_length + 4
                
            elif type == 16:
                if key == query_list[pointer]:
                    result = int.from_bytes(data[start:start+4], byteorder="little")
                start += 4
            
            elif type == 3:
                if key == query_list[pointer]:
                    query_helper(start, pointer+1)
                start += doc_length

    query_helper()
    return result

print(query('$.address.sector', 'test.bson'))
print(query('$.name', 'test.bson'))
print(query('$.mobile', 'test.bson'))

