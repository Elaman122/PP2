def un(a) :
    uniq = []
    for i in range(0, len(uniq)) :
        for j in range(0, len(uniq)) :
            if(a[i] != a[j]) :
                uniq.append(a[i])

    return uniq

print(un([1, 2, 3, 4, 5, 3, 5, 3]))
print(un([3, 'word', 'f' , 'word', 3 , 2, 4]))