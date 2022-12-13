#1712
"""
바닥에는 기둥만 세울 수 있다.

기둥은 바닥 위에 있거나 보의 한쪽 끝 부분 위에 있거나, 
또는 다른 기둥 위에 있어야 합니다.

보는 한쪽 끝 부분이 기둥 위에 있거나, 
또는 양쪽 끝 부분이 다른 보와 동시에 연결되어 있어야 합니다.
0 1 2 3


[[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
"""
def check(n, gi, bo):
    bool = True
    for x in range (n-1):
        for y in range (n-1):
            gic = gi[x][y]
            boc = bo[x][y]
            if gic == 1:
                if(y == 0 or gi[x][y-1] == 1 or bo[x][y] == 1 
                   or bo[x-1][y] == 1):
                    bool = True
                else:
                    return False
            if boc == 1:
                if (gi[x][y-1] == 1 or gi[x+1][y-1] == 1 
                    or (bo[x-1][y] == 1 and bo[x+1][y] == 1)):
                    bool = True
                else:
                    return False
    return bool
                    
                    
def result (n, gi, bo):
    res = []
    for x in range (n-1):
        for y in range (n-1):
            if gi[x][y] == 1:
                res.append([x,y,0])
            if bo[x][y] == 1:
                res.append([x,y,1])
    return res

def solution(n, build_frame):
    N = n + 2
    S = build_frame
    """
    for i in range (len(S)):
        S[i] = S[i].replace("[[", "")
        S[i] = S[i].replace("[", "")
        S[i] = S[i].replace("]]", "")
        S[i] = S[i].replace("]", "")
        S[i] = S[i].split(",")
        S[i] = list(map(int, S[i]))
    """
    gi = [[0]*N for _ in range(N)]
    bo = [[0]*N for _ in range(N)]
    
    for i in range (len(S)):
        x = S[i][0]
        y = S[i][1]
        how = S[i][2]
        if S[i][3] == 1:
            if how == 0:
                if (y == 0 or gi[x][y-1] == 1 or bo[x-1][y] == 1 
                    or bo[x][y] == 1):
                    gi[x][y] = 1
            else:
                if gi[x][y-1] == 1 or gi[x+1][y-1] == 1 or (
                  bo[x-1][y] == 1 and bo[x+1][y] == 1):
                    bo[x][y] = 1
        else:
            if how == 0:
                gi[x][y] = 0
                cc = check(N, gi, bo)
                if cc == False:
                    gi[x][y] = 1
            else:
                bo[x][y] = 0
                cc = check(N, gi, bo)
                if cc == False:
                    bo[x][y] = 1
    answer = result(N,gi,bo)
    return answer


n = 5
s1 = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
s2 = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
print(solution(n,s1))