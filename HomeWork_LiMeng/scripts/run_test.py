import time
import json
from volcenginesdkarkruntime import Ark
import asyncio
import re
from leetcode_oj.leetcode_tester import LeetCodeTester
from leetcode.rest import ApiException  # 确保导入 ApiException


fail_exec_num=0

client = Ark(
    api_key="7ef33307-7868-4ce0-9d62-2aa1c02b0fdf",
    base_url="https://ark.cn-beijing.volces.com/api/v3",
)

leetcode_session = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJfYXV0aF91c2VyX2lkIjoiMTY5MzEzMTciLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJhbGxhdXRoLmFjY291bnQuYXV0aF9iYWNrZW5kcy5BdXRoZW50aWNhdGlvbkJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJiZGFiMmFkMzRjNzFhNzQ4ZTNlNzk5ZTViM2VhNTI3MDI2MzAxOWMxMWRlMWMyMmFlOThlMWVjMjMzMzVjYWM2Iiwic2Vzc2lvbl91dWlkIjoiNzYzMDkzOTYiLCJpZCI6MTY5MzEzMTcsImVtYWlsIjoibWVuZy5saS5hcm9tYUBnbWFpbC5jb20iLCJ1c2VybmFtZSI6IjVsajRwREtHQ0MiLCJ1c2VyX3NsdWciOiI1bGo0cERLR0NDIiwiYXZhdGFyIjoiaHR0cHM6Ly9hc3NldHMubGVldGNvZGUuY29tL3VzZXJzLzVsajRwREtHQ0MvYXZhdGFyXzE3NDEyNjA5NTEucG5nIiwicmVmcmVzaGVkX2F0IjoxNzQxMzYwNDQ5LCJpcCI6IjgxLjE2OC44My43MCIsImlkZW50aXR5IjoiYjgwMWQ0OTRmMTIyNzkzYjA2MTI2MzZiZmEyMzRiOWMiLCJkZXZpY2Vfd2l0aF9pcCI6WyI0Y2FhYzMzNDE3ZGFkNGVlZjAzM2Y4YTY3NmQzNWI5MyIsIjgxLjE2OC44My43MCJdfQ.Cpjv7jR8ODKDoDO-ZoUSxHmyAmTRoyDtkr5sWAyseEg"
csrf_token = "yMIBMFrHKqCcJOeHFaLunHDGfKCqo8sS8Am0VJxwJkc839BHXopiL10LDgEoHeb4"


class RateLimiter:
    def __init__(self, rpm=100, tpm=2500):
        self.rpm = rpm
        self.tpm = tpm
        self.interval = 60 / rpm
        self.last_call = 0
        self.token_count = 0

    def wait_and_count(self, tokens):
        current_time = time.time()
        elapsed = current_time - self.last_call
        
        # RPM限速
        if elapsed < self.interval:
            time.sleep(self.interval - elapsed)
        
        # TPM限速
        if self.token_count + tokens > self.tpm:
            time.sleep(60 - (current_time % 60))
            self.token_count = 0
        
        self.last_call = time.time()
        self.token_count += tokens


# 生成修复后的代码
def generate_fix(buggy_code, description):
    limiter = RateLimiter()

    # 输入: buggy_code + description
    messages = [
        {"role": "system", "content": "你是一个专业程序员，请修复代码中的错误"},
        {"role": "user", "content": f"{description}. \n 请修复如下错误的代码：\n{buggy_code}"}
    ]
    
    limiter.wait_and_count(len(buggy_code.split()))  # 估算输入token
    response = client.chat.completions.create(
        model="ep-20250227111311-lmlfn",
        messages=messages,
        max_tokens=512
    )
    generated_code = response.choices[0].message.content
    limiter.token_count += len(generated_code.split())  # 估算输出token

    print("generated_code:",generated_code)
    return extract_code(generated_code)

def extract_code(text):
    # 提取Markdown代码块
    match = re.search(r'```python\n(.*?)\n```', text, re.DOTALL)
    return match.group(1) if match else text

passed_tests = 0
total_tests = 0

# 创建请求队列
request_queue = asyncio.Queue()

# 测试报告文件
report_file_path = 'test_report.html'

# 初始化序号
test_case_number = 1

async def process_requests():
    while not request_queue.empty():
        case = await request_queue.get()  # 从队列中获取请求
        await test_case(case)  # 处理请求
        request_queue.task_done()  # 标记请求处理完成
        
        # 暂停几秒钟，假设暂停2秒
        await asyncio.sleep(5)  # 休息2秒钟


async def test_case(case):
    global passed_tests
    buggy_code = case['buggy_code']
    task_id = case['slug']  
    description = case['description']
    
    tester = LeetCodeTester(leetcode_session=leetcode_session, csrf_token=csrf_token, cooldown=10)
    fixed_code = generate_fix(buggy_code,description)

    success = False  # 用于跟踪是否成功
    
    for attempt in range(3):  # 尝试最多 3 次
        try:
            result = await asyncio.to_thread(tester.test, fixed_code, task_id, "python")
            print(f"Result for task {task_id}: {result}")
            
            if result[0]:
                passed_tests += 1
                print(f"Test case {task_id} passed.")
                success = True  # 标记为成功
                # log_result(task_id, "pass")  # 记录成功
                break  # 成功则退出重试
            else:
                print(f"Test case {task_id} failed.")
                # log_result(task_id, "fail", fixed_code)  # 记录失败
                with open('failed_tests.txt', 'a') as f:
                    f.write(f"Task ID: {task_id}, Fixed Code\n: {fixed_code}\n")
            
        except ApiException as e:
            # if e.status == 429:  # 如果是 429 错误
            print("Rate limit exceeded. Retrying after a delay...")
            await asyncio.sleep(5)  # 等待 5 秒后重试
            print("task_id is:",task_id)
            with open('ApiException.txt', 'a') as f:
                    f.write(f"Task ID: {task_id}, Fixed Code: {fixed_code}\n")
            continue  # 继续处理下一个请求

    # 在所有尝试后，根据成功标记记录结果
    if success:
        log_result(task_id, "pass")  # 记录成功
    else:
        log_result(task_id, "fail", fixed_code)  # 记录失败        
  
    print(f"通过的测试用例数量: {passed_tests}/{total_tests}")



def log_result(task_id, status, fixed_code=None):
    global test_case_number
    with open(report_file_path, 'a') as report_file:
        if status == "pass":
            report_file.write(f"<p style='color: green;'>✅ {test_case_number}. Task ID: {task_id} - Status: PASS</p>\n")
        elif status == "fail":
            report_file.write(f"<p style='color: red;'>❌ {test_case_number}. Task ID: {task_id} - Status: FAIL</p>\n")
            report_file.write(f"<pre>Fixed Code: {fixed_code}</pre>\n")
        report_file.write("<hr>")  # 添加水平线以分隔每个测试结果
        
        test_case_number += 1  # 更新序号


async def main():
    global total_tests, passed_tests

    with open('/Users/aroma/Desktop/字节跳动面试题/DebugBench-main/benchmark/python3_double.json', 'r') as f:
        cleaned_data = json.load(f)

    # 提取前 200 条数据
    top_5_data = cleaned_data[:200]

    total_tests = len(top_5_data)
    passed_tests = 0  # 初始化通过的测试用例数量
    
    
    # 将请求添加到队列
    for case in top_5_data:
        await request_queue.put(case)

    # 处理请求
    await process_requests()


# 运行主函数
if __name__ == "__main__":

    # 初始化 HTML 报告文件
    with open(report_file_path, 'w') as report_file:
        report_file.write("<html><head><title>测试报告</title></head><body>")
        report_file.write("<h1>测试报告</h1>")


    asyncio.run(main())

    # 结束 HTML 报告文件
    with open(report_file_path, 'a') as report_file:
        report_file.write(f"<h3 style='color: blue;'>通过的测试用例数量: {passed_tests}/{total_tests}</h3>")  # 在报告最前面添加通过的数量
        report_file.write("</body></html>")

    print(f"通过的测试用例数量: {passed_tests}/{total_tests}")

