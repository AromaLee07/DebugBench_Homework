# DebugBench_Homework

### 说明

- **项目用途**：
1. 将论文中提到的大模型评测方法以流程图形式呈现，明确展示大模型的输入、输出以及评分方式；
2. 对项目代码进行完整复现，并使用提供的大模型API，批量运行评测集中所提供的数据（无需全部运行，自选200条左右即可），计算大模型的最终评测分数；
3. 对大模型的评测分数进行准确性校验，并撰写针对评分的准确性分析总结
   
- **项目文件使用说明**：
1. scripts/run_test.py 是对大模型的评测，该文件应该运行在项目的evaluation目录下，并且会使用leetcode相关的库和文件
2. scripts/caculate_scores.py 应该运行在 HomeWork_LiMeng目录下，用于生成大模型的评测分数
3. scripts/draw_fail.py 可以运行在任意目录下，可以画出大模型用例失败的原因
4. validate_failed_manually 目录下的代码，为手动运行失败的用例的结果，并且统计了失败原因，是对大模型做的准确性校验
   
- **项目文档说明**：
1. “流程图.jpg” 文件位要求的大模型评测方法的流程图，明确展示了大模型的输入、输出以及评分方式
2. “大模型评测结果.html” 为 scripts/run_test.py的运行结果，使用需求说明书里提到的大模型API，批量运行评测集中所提供的数据，所得到的运行结果，以列表的形式展示
3. “大模型评测分数.txt” 为 scripts/caculate_scores.py的运行结果，统计成功结果的占比
4. “大模型失败原因统计.png” 为 scripts/draw_fail.py的运行结果，统计的是所有失败的用例中，失败原因的统计，以饼图的形式体现
   
- **关于计算大模型的评测分数说明**：
1. 大模型的输入: buggy_code + description
2. 大模型针对输入，进行有效的输出，输出结果为修复后的代码
3. 使用leetcode线上评测系统，针对大模型生成的修复代码进行评测，返回评测分数：pass/(fail+pass), 实际得到的评测分数为 27/(92+27)=0.77
4. pass表示大模型生成的代码通过了leetcode的语法测试以及输入输出校验，fail表示的原因很复杂，也许是语法错误，也许是输出不符合预期，也可能误判 

- **针对评分的准确性分析总结**：
1. 对于已经通过了leetcode线上评测的输出，就算作输出完全没问题，不需要再做准确性分析
2. 对于没用通过leetcode线上评测的输出，在本地手动运行大模型返回的的fixed_code，结合case里的输入输出，进行验证
3. 如果运行代码不通过，则视为语法错误；如果验证返回的结果和预期结果相同，则判定为大模型的误判；如果验证返回的结果和预期结果不同，则判定逻辑错误
4. 随机挑选前13条失败的用例，结合上述手工运行的结果，误判为15.4%，语法错误为38.5%，逻辑错误为46.2%
5. 可以得出大模型的准确率大概为 (1-15.4%)=84.6%
6. 测试中发现误判的原因有的也很复杂，比如第56个case：construct-binary-tree-from-inorder-and-postorder-traversal：
      实际输出: Constructed Binary Tree: **3**, left: (**9**, left: (None), right: (**None**)), right: (**20**, left: (**15**, left: (None), right: (None)), right: (**7**, left: (None), right: (None))) \n
      预期输出: [3,9,20,null,null,15,7]
   其实是一致的，只是取决于何样的输出样式，这是人工决定的，所以算作误判
7. 综上所述，大模型的准确率是高于84.6%的，预计可能实际在92%左右


