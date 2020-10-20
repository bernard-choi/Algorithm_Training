def dfs(index, path):
    if len(path) == le(digits):
        result.append(path)
        return

    for i in range(index, len(digits)):
        for j in range(dic[digits[i]]):
            dfs(index + 1, path + j)



if __name__ == '__main__':
    digits = "23"
    path = ""
    dic = {"2": "abc", "3" : "def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxys"}
    result = []
    dfs(0,"")
    print(result)
