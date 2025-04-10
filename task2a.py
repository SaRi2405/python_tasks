# 1) 5, 10, 15, 20 rəqəmlərindən ibarət “rəqəmlər” adlı list yaradın
rəqəmlər = [5, 10, 15, 20]

# 2) “rəqəmlər” listinin uzunluğunu tapın
print(len(rəqəmlər))

# 3) “rəqəmlər” listinə 25 elementini əlavə edin
rəqəmlər.append(25)
print(rəqəmlər)

# 4) “rəqəmlər” listinin 2-ci indeksinə 12 elementini əlavə edin
rəqəmlər.insert(2, 12)
print(rəqəmlər)

# 5) 1, 2, 3 və 4, 5, 6 listlərini birləşdirin
list1 = [1, 2, 3]
list2 = [4, 5, 6]
birlesmis = list1 + list2
print(birlesmis)

# 6) “rəqəmlər” listindən 2-ci və 3-cü elementləri seçin
print(rəqəmlər[2:4])

# 7) “rəqəmlər” listinin ilk elementini 50 ilə əvəz edin 
rəqəmlər[0] = 50
print(rəqəmlər)

# 8) “rəqəmlər” listində 19 elementinin olub-olmadığını yoxlayın
print(19 in rəqəmlər)

# 9) "a", "b", "a", "c" listində "a" elementinin neçə dəfə təkrarlandığını tapın
simvollar = ["a", "b", "a", "c"]
print(simvollar.count("a"))

# 10) "x", "y", "x", "z" listindən "x" elementlərini silin
simvollar2 = ["x", "y", "x", "z"]
simvollar2 = [i for i in simvollar2 if i != "x"]
print(simvollar2)

# 11) 7, 2, 9, 1 listini azalan sırayla sıralayın
nums = [7, 2, 9, 1]
nums.sort(reverse=True)
print(nums)

# 12) “rəqəmlər” listindən 10-dan böyük elementləri seçin
boyukler = [i for i in rəqəmlər if i > 10]
print(boyukler)
