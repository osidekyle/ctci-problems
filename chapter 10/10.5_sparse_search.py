

def sparseSearch(target, words, start, end):
    mid = (start + end) // 2
    if start > end:
        return None

    if words[mid] == "":
        left = mid - 1
        right = mid + 1
        while True:
            if left < start or right > end:
                return None
            if words[left] != "":
                mid = left
                break
            if words[right] != "":
                mid = right
                break
            left -= 1
            right += 1

    if words[mid] == target:
        return mid
    elif words[mid] < target:
        return sparseSearch(target, words, mid + 1, end)
    else:
        return sparseSearch(target, words, start, mid)


print(sparseSearch("car", ["", "", "", "ball", "", "", "car", "", "", "dad", "", ""], 0, 12))

