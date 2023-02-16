import json
def structureData(data):
    sendData = str(data).split('{')
    sendData = sendData[1].split(',')
    inputData = dict()
    for i in sendData:
      try:
        key,value = i.split(':')
        key = eval(key)
        value=eval(value)
        try:
            inputData[key] =int(value)
        except:
            inputData[key] = value
      except:
        value = eval(value.split("}")[0])
        inputData[key] = int(value)
    sendData = inputData
    data = sendData
    f = open('labels1.json')
    label_list = []
    labels = dict(json.load(f))
    for i,j in labels.items():
        print(i,j)
    for i,j in data.items():
        if type(j)==type('str'):
            label_list.append([i,j])
    print(label_list)
    for i in label_list:
        col,val = i
        data[col] = labels[col.upper()][val.upper()]
    print(list(data.values()))
    return list(data.values())