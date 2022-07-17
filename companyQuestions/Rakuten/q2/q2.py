class Solution():


    def create_matrix(self,N, M, Q, query):
        rows = []
        mat=[]
        for i in range(0,N):
            for j in range(0,M):
                rows.append(0)
            mat.append(rows)
            rows=[]

        for i in range(0,Q):
            j = query[i][1]
            k = query[i][2]
            right_or_left = query[i][0]

            if right_or_left == 0:
                for col in range(0,k):
                    mat[j-1][col] = 1

            elif right_or_left == 1:
                for col in range(k-1,M):
                    mat[j-1][col] = 1
        return mat


    def is_safe(self,newx, newy, mat, N, M, visited):
        if ((newx >= 0 and newx < N) and (newy >= 0 and newy < M) and (visited[newx][newy] == 0) and (mat[newx][newy] == 0)):
            return True
        return False


    def find_possible_paths(self,x, y, mat, N, M, visited, ans, path):
        if x == N-1 and y == M-1:
            ans.append(len(path))
            return

        visited[x][y] = 1

        #down
        newx = x + 1
        newy = y
        if self.is_safe(newx, newy, mat, N,M, visited):
            path += "D"
            self.find_possible_paths(newx, newy, mat,N, M, visited, ans, path)
            path = path[:-1]

        # up
        newx = x - 1
        newy = y
        if self.is_safe(newx, newy, mat, N,M, visited):
            path += "U"
            self.find_possible_paths(newx, newy, mat,N, M, visited, ans, path)
            path = path[:-1]

        # right
        newx = x
        newy = y + 1
        if self.is_safe(newx, newy, mat, N,M, visited):
            path += "R"
            self.find_possible_paths(newx, newy, mat, N,M, visited, ans, path)
            path = path[:-1]

        # left
        newx = x
        newy = y - 1
        if self.is_safe(newx, newy, mat, N,M, visited):
            path += "L"
            self.find_possible_paths(newx, newy, mat, N,M, visited, ans, path)
            path = path[:-1]

        visited[x][y] = 0


    def solve(self,N,M,Q,query,r,c):
        mat = self.create_matrix(N,M,Q,query)
        # initialize visited array
        v = []
        visited = []
        for i in range(0, N):
            for j in range(0, M):
                v.append(0)
            visited.append(v)
            v = []

        ans = []
        path = ""
        x = r-1
        y = c-1
        visited[x][y] = 1

        self.find_possible_paths(x,y,mat,N,M,visited,ans,path)

        if len(ans) == 0:
            return -1
        return min(ans)

print(Solution().solve(2,6,2,[[1,1,5],[0,2,2]],1,3))
print(Solution().solve(4,5,5,[[1,1,4],[0,2,2],[1,2,5],[0,3,1],[1,3,4]],1,2))