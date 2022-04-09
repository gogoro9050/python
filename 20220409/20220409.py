# bool( )檢查括號內是否有東西
# int(  )變成整數
# str(  )變成字串
# float(  )變成小數
# round(  )四捨五入
# import 匯入模組
# install 安裝

# 運算元:進行運算的數字或資料
# 運算子:進行運算的方法
# 例如:(1+2)中的1跟2為運算元，+號為運算子

# 一元運算子:
# 取負數-
# 取正數+

# 二元運算子:
# 加法+
# 減法-
# 乘法*
# 小數除法/
# 整數除法//
# 取餘數%
# 次方**

# 算出圓的面積(半徑*半徑*3.14):
# ans = int(input('圓的半徑'))
# pi = 3.14
# print(ans * ans * pi)

# import matplotlib  #匯入matplotlib模組

# 以下為顯示圖片的程式:
import matplotlib.pyplot as plt
import matplotlib.image as img

image = img.imread('20220409/logo-unite.png')  #圖片的路徑
plt.imshow(image)
plt.show()