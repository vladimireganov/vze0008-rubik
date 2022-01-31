import rubik.cube as rubik

def _check(parms):
    result={}
    key = {}
    encodedCube = parms.get('cube',None)       
    if(encodedCube == None):
        result['status'] = 'error: xxx'
        return result
    elif (not(isinstance(encodedCube, str))):
        result['status'] = 'error: not str'
        return result 
    elif ( len (encodedCube)!= 54):
        result['status'] = 'error: len'
        return result
    for i in range(len(encodedCube)):
        if encodedCube[i] in key:
            key[encodedCube[i]] += 1
        else: 
            key[encodedCube[i]] = 1
    if len(key) != 6:
        result['status'] = 'error: not 6 unique'
        return result
    for i in key:
        if key[i] != 9:
            result['status'] = 'error: not 9 occurences'
            return result
    middle_face = []
    middle_face.append(encodedCube[4])
    middle_face.append(encodedCube[14])
    middle_face.append(encodedCube[23])
    middle_face.append(encodedCube[32])
    middle_face.append(encodedCube[41])
    middle_face.append(encodedCube[50])
    
    for i in range(5):
        if middle_face[i+1] == middle_face[0]:
            result['status'] = 'error: middle face diff color'
            return result
    for i in range(4):
        if middle_face[i+2] == middle_face[1]:
            result['status'] = 'error: middle face diff color'
            return result
    for i in range(3):
        if middle_face[i+3] == middle_face[2]:
            result['status'] = 'error: middle face diff color'
            return result
    if middle_face[3] == middle_face[4]:
            result['status'] = 'error: middle face diff color'
            return result
    elif middle_face[3] == middle_face[5]:
            result['status'] = 'error: middle face diff color'
            return result
    elif middle_face[4] == middle_face[5]:
            result['status'] = 'error: middle face diff color'
            return result
    
    result['status'] = 'ok'
    return result