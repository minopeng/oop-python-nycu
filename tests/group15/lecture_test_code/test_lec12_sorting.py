import pytest
import lec12_sorting as S  # 匯入要測試的模組，並簡稱為 S

# ==========================================
# 測試資料裝飾器 (Decorator)
# @pytest.mark.parametrize 用來定義多組測試輸入。
# 下面的測試函式會被執行多次，每次 'arr' 變數會帶入列表中的不同值。
# 測試案例包含了：空陣列、單一元素、已排序、反序、包含負數與重複值等邊界情況。
# ==========================================
@pytest.mark.parametrize(
    "arr",
    [
        [],                 # 空列表
        [1],                # 單一元素
        [2, 1],             # 簡單反序
        [1, 2, 3],          # 已排序
        [3, 2, 1],          # 反序
        [5, -1, 3, 3, 0, -1], # 亂序、包含負數、包含重複值
        [2, 2, 2, 2],       # 全部重複
    ],
)
def test_bubble_sort_returns_sorted_and_mutates(arr, capsys):
    """
    測試氣泡排序 (Bubble Sort)：
    1. 必須回傳排序好的列表 (Returns sorted)。
    2. 必須修改原本的列表 (Mutates/In-place)。
    """
    a = arr[:]  # 複製一份列表，避免修改到原本的測試資料 'arr'
    out = S.bubble_sort(a) # 執行排序
    
    _ = capsys.readouterr().out  # 讀取並清空終端機輸出 (這裡不檢查輸出內容，只清空緩衝區)
    
    assert out == sorted(arr)  # 驗證：回傳的結果必須是排序好的
    assert a == sorted(arr)    # 驗證：傳入的變數 'a' 本身必須被修改成排序好的狀態
    assert out is a            # 關鍵驗證：檢查物件記憶體位址。要求函式必須回傳 'a' 本身 (return L)，而非新列表。


@pytest.mark.parametrize(
    "arr",
    [
        [], [1], [2, 1], [1, 2, 3], [3, 2, 1], [5, -1, 3, 3, 0, -1], [2, 2, 2, 2],
    ],
)
def test_selection_sort_inplace_and_prints(arr, capsys):
    """
    測試選擇排序 (Selection Sort)：
    1. 必須是原地排序 (In-place)。
    2. 必須回傳 None (不可以有 return 值)。
    3. 必須在執行過程中 print 出特定字串。
    """
    a = arr[:]
    ret = S.selection_sort(a)
    
    # capsys 是 pytest 的功能，用來捕捉函式執行過程中的 print 內容
    out = capsys.readouterr().out 
    
    assert ret is None         # 驗證：這個實作必須沒有回傳值 (return None)
    assert a == sorted(arr)    # 驗證：變數 'a' 必須被修改為已排序
    assert "selection sort:" in out or arr == [] # 驗證：必須印出 "selection sort:" (除非列表是空的)


@pytest.mark.parametrize(
    "left,right,expected",
    [
        ([], [], []),                  # 兩個空列表
        ([1], [], [1]),                # 左邊有，右邊空
        ([], [1], [1]),                # 左邊空，右邊有
        ([1, 3, 5], [2, 4, 6], [1, 2, 3, 4, 5, 6]), # 標準交錯合併
        ([1, 2, 2], [2, 2, 3], [1, 2, 2, 2, 2, 3]), # 包含重複值
        ([-3, -1, 2], [-2, 0, 1], [-3, -2, -1, 0, 1, 2]), # 負數
    ],
)
def test_merge_print_version(left, right, expected, capsys):
    """
    測試合併 (Merge) 輔助函式：
    驗證是否能將兩個「已排序」的列表，合併成一個新的有序列表。
    """
    out = S.merge(left, right)
    _ = capsys.readouterr().out # 忽略輸出
    assert out == expected      # 驗證結果是否符合預期


@pytest.mark.parametrize(
    "arr",
    [
        [], [1], [2, 1], [1, 2, 3], [3, 2, 1], [5, -1, 3, 3, 0, -1], [2, 2, 2, 2],
    ],
)
def test_merge_sort_print_version(arr, capsys):
    """
    測試合併排序 (Merge Sort)：
    1. 必須回傳一個新的排序列表。
    2. 不可以修改原本的列表 (Not In-place)。
    3. 必須有 print 輸出。
    """
    a = arr[:]
    out = S.merge_sort(a)
    printed = capsys.readouterr().out
    
    assert out == sorted(arr)  # 驗證：回傳結果已排序
    assert a == arr            # 關鍵驗證：原本的 'a' 必須保持原樣 (未被修改)
    assert "merge sort:" in printed or arr == [] # 驗證：必須有特定的 print 輸出


# ==========================================
# 下方皆為 "_np" (No Print) 版本的測試
# 邏輯與上方相同，但嚴格要求「不可以 print 任何東西」
# ==========================================

@pytest.mark.parametrize(
    "arr",
    [
        [], [1], [2, 1], [1, 2, 3], [3, 2, 1], [5, -1, 3, 3, 0, -1], [2, 2, 2, 2],
    ],
)
def test_bubble_sort_np_silent_and_sorted(arr, capsys):
    """測試靜音版氣泡排序：邏輯正確且完全沒有輸出"""
    a = arr[:]
    out = S.bubble_sort_np(a)
    printed = capsys.readouterr().out
    
    assert out == sorted(arr)
    assert a == sorted(arr)     # In-place 修改
    assert printed.strip() == "" # 驗證：截去空白後必須是空字串 (即沒有 print)


@pytest.mark.parametrize(
    "arr",
    [
        [], [1], [2, 1], [1, 2, 3], [3, 2, 1], [5, -1, 3, 3, 0, -1], [2, 2, 2, 2],
    ],
)
def test_selection_sort_np_inplace_and_silent(arr, capsys):
    """測試靜音版選擇排序：原地修改、回傳 None、且完全沒有輸出"""
    a = arr[:]
    ret = S.selection_sort_np(a)
    printed = capsys.readouterr().out
    
    assert ret is None
    assert a == sorted(arr)
    assert printed.strip() == "" # 驗證：沒有 print


@pytest.mark.parametrize(
    "left,right,expected",
    [
        ([], [], []),
        ([1], [], [1]),
        ([], [1], [1]),
        ([1, 3, 5], [2, 4, 6], [1, 2, 3, 4, 5, 6]),
        ([1, 2, 2], [2, 2, 3], [1, 2, 2, 2, 2, 3]),
        ([-3, -1, 2], [-2, 0, 1], [-3, -2, -1, 0, 1, 2]),
    ],
)
def test_merge_np(left, right, expected, capsys):
    """測試靜音版 Merge 函式"""
    out = S.merge_np(left, right)
    printed = capsys.readouterr().out
    
    assert out == expected
    assert printed.strip() == "" # 驗證：沒有 print


@pytest.mark.parametrize(
    "arr",
    [
        [], [1], [2, 1], [1, 2, 3], [3, 2, 1], [5, -1, 3, 3, 0, -1], [2, 2, 2, 2],
    ],
)
def test_merge_sort_np(arr, capsys):
    """測試靜音版合併排序：建立新列表、不修改原列表、且完全沒有輸出"""
    a = arr[:]
    out = S.merge_sort_np(a)
    printed = capsys.readouterr().out
    
    assert out == sorted(arr)
    assert a == arr             # 驗證：原列表未被修改
    assert printed.strip() == "" # 驗證：沒有 print
