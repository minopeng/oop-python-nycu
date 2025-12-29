# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 12:13:13 2016

@author: ericgrimson
"""

# ==========================================
# 第一種二分搜尋法 (Binary Search) - 切片法
# 缺點：每次遞迴都會複製列表 (L[:half])，時間複雜度較高 O(N)
# ==========================================
def bisect_search1(L, e):
    # 僅為了觀察程式執行過程，印出當前列表的第一個和最後一個元素
    # 注意：如果列表為空，這裡會報錯，但因為下方先判斷了 L == []，所以在這之前可能需要防呆
    if L == []:
        return False
    # 若這裡才印出可能比較安全，或者先確認 L 不為空
    print('low: ' + str(L[0]) + '; high: ' + str(L[-1]))

    if L == []:
        return False
    elif len(L) == 1:
        # 基礎情況 (Base case)：剩一個元素時，檢查是否為目標 e
        return L[0] == e
    else:
        half = len(L) // 2  # 找出中間索引
        if L[half] > e:
            # 如果中間值比目標大，表示目標在左半邊
            # 注意：L[:half] 會產生一個新的列表 (Copy)，這在 Python 中成本較高
            return bisect_search1(L[:half], e)
        else:
            # 如果中間值比目標小 (或等於)，表示目標在右半邊
            return bisect_search1(L[half:], e)

# ==========================================
# 第二種二分搜尋法 - 索引法 (更有效率)
# 優點：不複製列表，只傳遞索引 (low, high)，空間複雜度 O(1)
# ==========================================
def bisect_search2(L, e):
    # 定義一個內部的輔助函式，負責遞迴邏輯
    def bisect_search_helper(L, e, low, high):
        print('low: ' + str(low) + '; high: ' + str(high))  # 視覺化目前的搜尋範圍索引
        
        # 基礎情況：範圍縮小到起點等於終點
        if high == low:
            return L[low] == e
        
        mid = (low + high) // 2  # 計算中間索引
        
        if L[mid] == e:
            return True  # 找到了！
        elif L[mid] > e:
            # 目標在左半邊
            if low == mid: # 如果範圍已經無法再縮小 (nothing left to search)
                return False
            else:
                # 搜尋範圍改為 [low, mid - 1]
                return bisect_search_helper(L, e, low, mid - 1)
        else:
            # 目標在右半邊，搜尋範圍改為 [mid + 1, high]
            return bisect_search_helper(L, e, mid + 1, high)
            
    # 主函式入口
    if len(L) == 0:
        return False
    else:
        # 呼叫輔助函式，初始範圍為 0 到 列表長度-1
        return bisect_search_helper(L, e, 0, len(L) - 1)

# --- 測試二分搜尋法 ---
testList = []
for i in range(100):
    testList.append(i) # 建立一個 0 到 99 的列表

# 尋找數字 76
print(bisect_search1(testList, 76))
print(bisect_search2(testList, 76))


# ==========================================
# 產生所有子集 (Generate Subsets)
# 概念：遞迴找出「不包含最後元素」的所有子集，然後將它們「加上最後元素」
# ==========================================
def genSubsets(L):
    res = []
    # 基礎情況：空列表的子集只有一個，就是空列表本身
    if len(L) == 0:
        return [[]] # list of empty list
        
    # 遞迴步驟：
    # 1. smaller: 先算出「不包含最後一個元素」的所有子集
    #    例如 L=[1,2]，這裡會算出 [1] 的子集 -> [[], [1]]
    smaller = genSubsets(L[:-1]) 
    
    # 2. extra: 取得最後一個元素，並轉為列表格式
    extra = L[-1:] 
    
    new = []
    # 3. 組合：
    #    對於 smaller 中的每一個子集，都把 extra (最後一個元素) 加進去
    #    例如 smaller 是 [[], [1]]，extra 是 [2]
    #    new 就會變成 [[2], [1, 2]]
    for small in smaller:
        new.append(small + extra) 
        
    # 4. 回傳：原本的子集 (不含extra) + 新的子集 (含extra)
    #    回傳 [[], [1], [2], [1, 2]]
    return smaller + new 

# --- 測試子集生成 ---
testSet = [1, 2, 3, 4]
print(genSubsets(testSet))
