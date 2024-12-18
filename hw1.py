#原創

from datetime import datetime
power2n=[None]*1000
power2n[0]=1
power2n[1]=2
# 方法 1
def power2n_a(n):
    return 2**n

# 方法 2：用遞迴+查表
def power2n_d(n):
    if n < 0: raise
    if not power2n[n] is None: return power2n[n]
    power2n[n] = power2n_d(n-1)+power2n_d(n-1)
    return power2n[n]

print(f'power2n_d={power2n_d(12)}')
