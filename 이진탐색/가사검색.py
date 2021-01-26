from bisect import bisect_left,bisect_right
words=["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries=["fro??", "????o", "fr???", "fro???", "pro?"]
words.sort(key= lambda x: len(x))
def find_idxs(target,flag,q_num,r_str,w_l,rw_l):
  front=""
  end=""
  if(flag==0):
    front+=r_str
    end+=r_str
    for _ in range(q_num):
      front+='a'
      end+='z'
    fidx=bisect_left(rw_l[len(target)],target[::-1].replace('?','a'))
    eidx=bisect_right(rw_l[len(target)],target[::-1].replace('?','z'))
  else:
    front += r_str
    end += r_str
    for _ in range(q_num):
      front += 'a'
      end += 'z'
    fidx = bisect_left(w_l[len(target)], target.replace('?','a'))
    eidx = bisect_right(w_l[len(target)], target.replace('?','z'))
  return fidx,eidx

def solution(words, queries):
  answer = []
  w_l=[[]for _ in range(10001)]
  rw_l=[[]for _ in range(10001)]
  for w in words:
    w_l[len(w)].append((w))
    rw_l[len(w)].append(w[::-1])
  for l in w_l:
    l.sort()
  for l in rw_l:
    l.sort()
  for q in queries:
    q_num=0
    r_str=""
    if(q[0]=='?'):
      flag=0
    else:
      flag=1
    for w in q:
      if(w!="?"):
        r_str+=w
      else:
        q_num+=1
    f_idx,e_idx=find_idxs(q,flag,q_num,r_str,w_l,rw_l)
    answer.append(e_idx-f_idx)

  return answer

print(solution(words,queries))