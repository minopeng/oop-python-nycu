# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 12:13:13 2016

@author: ericgrimson
"""

# ==============================================================================
# 版本一：使用列表切片 (List Slicing) 的二分搜尋
# 缺點：L[:half] 和 L[half:] 會複製列表，導致額外的記憶體開銷與 O(N) 的複製時間，
# 使得整體效率不如標準的 O(log N)。
# ==============================================================================
def bisect_search1(L, e):
    # 印出目前搜尋範圍的頭尾元素 (注意：若 L 一開始為空，這裡存取索引會報錯)
    print('low: ' + str(L[0]) + '; high: ' + str(L[-1]))
    
    # 基礎情況 (Base Cases)
    if L == []:
        return False  # 列表為空，找不到
    elif len(L) == 1:
        return L[0] == e  # 只剩一個元素，檢查是否相等
    else:
        # 遞迴步驟 (Recursive Step)
        half = len(L)//2  # 找出中間索引
        if L[half] > e:
            # 中間值比目標大 -> 搜尋左半邊 (複製左半列表傳入)
            return bisect_search1(L[:half], e)
        else:
            # 中間值比目標小 (或相等) -> 搜尋右半邊 (複製右半列表傳入)
            return bisect_search1(L[half:], e)

# ==============================================================================
# 版本二：使用索引邊界 (Indices) 的二分搜尋
# 優點：這是標準且高效的寫法。只傳遞索引值 (low, high)，不複製列表，
# 空間複雜度 O(1)，時間複雜度 O(log N)。
# ==============================================================================
def bisect_search2(L, e):
    # 定義內部的輔助函式，負責遞迴邏輯
    def bisect_search_helper(L, e, low, high):
        print('low: ' + str(low) + '; high: ' + str(high))  # 視覺化目前的索引範圍
        
        # 基礎情況：範圍縮小到起點等於終點
        if high == low:
            return L[low] == e
        
        mid = (low + high)//2  # 計算中間索引
        
        if L[mid] == e:
            return True  # 找到了
        elif L[mid] > e:
            # 目標在左半邊
            if low == mid: # 如果範圍已經無法再縮小 (例如剩兩個元素時)
                return False
            else:
                # 搜尋範圍改為 [low, mid - 1]
                return bisect_search_helper(L, e, low, mid - 1)
        else:
            # 目標在右半邊，搜尋範圍改為 [mid + 1, high]
            return bisect_search_helper(L, e, mid + 1, high)
    
    # 主函式邏輯
    if len(L) == 0:
        return False
    else:
        # 呼叫輔助函式，初始範圍為 0 到 列表長度-1
        return bisect_search_helper(L, e, 0, len(L) - 1)

# --- 測試二分搜尋 ---
testList = []
for i in range(100):
    testList.append(i) # 建立 0 到 99 的列表

# 尋找數字 76
print("--- Search 1 ---")
print(bisect_search1(testList, 76))
print("\n--- Search 2 ---")
print(bisect_search2(testList, 76))


# ==============================================================================
# 產生所有子集 (Generate Subsets / Power Set)
# 邏輯：一個集合 S 的所有子集 = (S 去掉最後元素 x 的所有子集) + (那些子集加上 x)
# ==============================================================================
def genSubsets(L):
    res = []
    # 基礎情況：空列表的子集只有一個，就是空列表本身 [[]]
    if len(L) == 0:
        return [[]] # list of empty list
    
    # 遞迴呼叫：取得「不包含最後一個元素」的所有子集
    # 例如 L=[1,2]，這裡會先算出 [1] 的子集 -> [[], [1]]
    smaller = genSubsets(L[:-1]) 
    
    # 取得最後一個元素，並轉為列表 (為了方便相加)
    extra = L[-1:] 
    
    new = []
    # 核心邏輯：
    # 將 smaller 中的每一個子集，都加上 extra (最後一個元素)
    # 例如 smaller=[[], [1]], extra=[2] -> new=[[2], [1, 2]]
    for small in smaller:
        new.append(small+extra)  
        
    # 回傳：原本的子集 (不含extra) + 新的子集 (含extra)
    return smaller+new 


# --- 測試子集生成 ---
testSet = [1,2,3,4]
print("\n--- Subsets ---")
print(genSubsets(testSet))
