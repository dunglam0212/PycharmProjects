def giai_thua(n):
    gt = 1
    for i in range(1,n+1):
        gt = gt*i
    return gt

def to_hop(k,n):
    return (giai_thua(n)/(giai_thua(k)*giai_thua(n-k)))

def xac_suat_den_hu(N,D,M):
    """
    N: số bóng đèn có trong mỗi hộp
    D: số bóng đèn hư có trong mỗi hộp
    M: số bóng đèn chọn ngẫu nhiên trong số N bóng đèn
    """
    return (D*to_hop((M-1),(N-D)))/(to_hop(M,N))
