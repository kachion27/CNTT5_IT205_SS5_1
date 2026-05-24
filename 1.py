branch_count = int(input("Nhập số lượng chi nhánh: "))
month_count = 3

all_branches_revenue = []

for branch in range(1, branch_count + 1):
    branch_revenue = []  
    for month in range(1, month_count + 1):
        revenue = int(input(f"Nhập doanh thu Chi nhánh {branch}, tháng {month}: "))
        branch_revenue.append(revenue)
        
    all_branches_revenue.append(branch_revenue)

for branch in range(1, branch_count + 1): 
    for month in range(1, month_count + 1):
        current_revenue = all_branches_revenue[branch - 1][month - 1]
        print(f"  Tháng {month}: {current_revenue} triệu đồng")
'''
Code cũ vòng lặp ngoài duyệt theo month (tháng) và vòng lặp trong duyệt theo branch (chi nhánh).
Do đó, chương trình sẽ cố định Tháng 1 rồi duyệt qua lần lượt Chi nhánh 1, Chi nhánh 2, Chi nhánh 3.
Vòng lặp ngoài nên duyệt theo chi nhánh (branch).
'''