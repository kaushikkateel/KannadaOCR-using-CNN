

def sequence(ImgDict):
    
    chars=str()
    
    keys = ImgDict.keys()
    
    sorted_input = sorted(keys)
    
    i = 0
    
    while(i < len(sorted_input)):
        
        line = sorted_input[i][:2]
       
        j = i
       
        while(j < len(sorted_input) and sorted_input[j][:2] == line):
            word = sorted_input[j][3:5]
           
            k = j
           
            while(k < len(sorted_input) and sorted_input[k][3:5] == word and sorted_input[k][:2] == line):
               
                chars += ImgDict[sorted_input[k]]
                k+=1
                
            j = k
            chars+=" "
           
        i = j
        chars+= "\n"
        
    return(chars)

# dictt={"1_1_1.JPG":"A","1_1_2.JPG":"B","1_2_1.JPG":"C","2_2_2.JPG":"D","2_1_1.JPG":"E",}
# c = sequence(dictt)
# print(c)