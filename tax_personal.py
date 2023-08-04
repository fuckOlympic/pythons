import os

#这里是一个使用 Python 计算深圳个人所得税的函数:
#python


def calc_sz_personal_income_tax(income):
    """计算深圳个人所得税"""
    # 税率对应税收区间
    tax_rule = [
        (0, 1500, 0.03),
        (1500, 4500, 0.1),
        (4500, 9000, 0.2),
        (9000, 35000, 0.25),
        (35000, 55000, 0.3),
        (55000, 80000, 0.35),
        (80000, float('inf'), 0.45) 
    ]
    
    # 累计税收
    total_tax = 0  
    
    # 当前区间
    current_section = 0 
    
    for i in range(len(tax_rule)):
        if income <= tax_rule[i][1]:
            current_section = i
            break
    
    # 计算当前区间税收
    total_tax += (tax_rule[current_section][1] - tax_rule[current_section][0]) * tax_rule[current_section][2]
    
    # 计算下一区间税收
    if current_section < len(tax_rule) - 1:
        next_section = current_section + 1
        total_tax += (income - tax_rule[current_section][1]) * tax_rule[next_section][2]
    
    # 减除速算扣除数
    total_tax -= 5400
   
    return round(total_tax)
    
"""
这个函数主要逻辑如下:
1. 定义深圳个税的税率区间和税率阶梯 in  tax_rule
2. 初始化累计税收 total_tax 和当前区间 current_section 变量
3. 根据納税者的收入 income 确定所在的税率区间 current_section
4. 计算当前区间税收,并加到 total_tax
5. 如果未超出最高区间,还需要计算下一区间的税收,继续加到 total_tax
6. 从 total_tax 中减除速算扣除数 5400 元
7. 返回最终累计税收 total_tax
8. 使用 round() 函数对税收结果四舍五入到整元这是一个比较标准的模拟税收计算的函数实现,首先定义好税率规则,
然后逐步判断納税收入所处的税率区间和计算对应区间的税收,最终汇总得出总的应纳税收入。希望这个实现能够帮助你理解个人所得税的计算过程。
如果对税收计算还有其他问题,也欢迎随时提问


"""
#input("Press Enter key to...")
os.system("pause");