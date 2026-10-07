"""バブルソートの実装例。"""


def bubble_sort(values):
    """リストを昇順に並べ替えた新しいリストを返す。

    隣り合う要素を比較して大きい方を後ろへ移動させる処理を繰り返す。
    1 回の走査で一度も交換が起きなければ、整列済みとみなして終了する。
    """
    result = list(values)
    n = len(result)
    for i in range(n - 1):
        swapped = False
        # 走査ごとに末尾 i 個は確定しているので比較対象から外す
        for j in range(n - 1 - i):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
                swapped = True
        if not swapped:
            break
    return result


if __name__ == "__main__":
    data = [64, 34, 25, 12, 22, 11, 90]
    print("ソート前:", data)
    print("ソート後:", bubble_sort(data))
