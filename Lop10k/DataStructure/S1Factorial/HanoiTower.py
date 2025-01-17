def hanoi_tower(n,A,B,C):
    """
    Đây là giải thuật đệ quy cho bài toán tháp Hà Nội
    :param n: là số đĩa cần di chuyển từ cột A qua cột C với cột B làm trung gian
    :param A: là cột nguồn chứa n đĩa ban đầu cần chuyển qua cột C
    :param B: là cột trung gian để trung chuyển đĩa do: chỉ chuyển 1 đĩa 1 lần và đĩa nhỏ nằm ở trên
    :param C: là cột đích sẽ nhận n đĩa từ cột A
    :return:
    """
    if n==1: #Điểm dừng
        print(f'Move {A} ==> {C}')
    else:
        hanoi_tower(n-1,A,C,B)
        print(f'Move {A} ==> {C}')
        hanoi_tower(n-1,B,A,C)

hanoi_tower(3,'A','B','C')