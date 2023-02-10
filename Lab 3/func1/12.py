def histogram(w) :
    soz = ""
    for i in range(0, len(w)) :
        for j in range(0, w[i]) :
            soz += "*"
        print(soz)
        soz = "" 


histogram([4, 9, 7])       
