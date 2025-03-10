# 读取 HTML 文件并统计成功和失败的任务数量
def count_test_results(file_path):
    success_count = 0
    fail_count = 0

    fail_str = 'Status: FAIL'
    pass_str = 'Status: PASS'
    
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            if pass_str in line:
                success_count += 1
            elif fail_str in line:
                fail_count += 1
    
    return success_count, fail_count

# 指定 HTML 文件路径
file_path = '/Users/aroma/Desktop/字节跳动面试题/DebugBench-main/HomeWork_LiMeng/大模型评测结果.html'
success, fail = count_test_results(file_path)

print(f"成功的任务数量: {success}")
print(f"失败的任务数量: {fail}")
# 计算总分数并格式化到小数点后两位
total_score = success / (success + fail)
print('总的分数: {:.2f}'.format(total_score))