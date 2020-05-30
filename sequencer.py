

def sequence(ImgDict):
    
    chars=str()
    
    keys = ImgDict.keys()
    
    sorted_input = sorted(keys)
    
    i = 0
    
    while(i < len(sorted_input)):
        
        line = sorted_input[i][3:5]
       
        j = i
       
        while(j < len(sorted_input) and sorted_input[j][3:5] == line):
            word = sorted_input[j][5:7]
           
            k = j
           
            while(k < len(sorted_input) and sorted_input[k][5:7] == word and sorted_input[k][3:5] == line):
               
                chars += ImgDict[sorted_input[k]]
                k+=1
                
            j = k
            chars+=" "
           
        i = j
        chars+= "\n"
        
    return(chars)

# dictt={"img1_1_1.JPG":"A","img1_1_2.JPG":"B","img1_2_1.JPG":"C","img2_2_2.JPG":"D","img2_1_1.JPG":"E",}
# c = sequence(dictt)
# print(c)