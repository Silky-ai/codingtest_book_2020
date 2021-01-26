str1=input()
str2=input()

len1=len(str1)
len2=len(str2)
mat=[[0]*(len1+1) for _ in range(len2+1)]

for i in range(len1+1):
  mat[0][i]=i
for j in range(len2+1):
  mat[j][0]=j

for i in range(1,len2+1):
  for j in range(1,len1+1):
    if(str1[j-1]==str2[i-1]):
      mat[i][j]=mat[i-1][j-1]
    else:
      mat[i][j]=min(mat[i-1][j-1]+1,mat[i-1][j]+1,mat[i][j-1]+1)
print(mat[len2-1][len1-1])
print(mat)
