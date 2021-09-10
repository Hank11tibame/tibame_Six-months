abc = 'abcdefghijklmnopqrstuvwxyz'
encry_dict = {}
front3 = abc[:3]
end23 = abc[3:]
subText = end23 + front3
encry_dict = dict(zip(abc, subText))
print("列印編碼字典\n", encry_dict)
msgTest = input("請輸入原始字串 :")
cipher = []
for i in msgTest:
    v = encry_dict[i]
    cipher.append(v)

ciphertext = ''.join(cipher)

print("原始字串",msgTest)
print("加密字串",ciphertext)
