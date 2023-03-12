# 计算 Transaction throughput（每分钟完成的事务数）
def calculate_tpm(transactions, duration):
    tpm = transactions / duration
    return tpm

# 计算 Price/performance ratio（系统性能和成本的比率）
def calculate_price_performace(cost, tpm):
    price_performance = cost / tpm
    return price_performance

# 计算 Average response time（平均响应时间）
def calculate_response_time(transactions, duration):
    response_time = duration / transactions
    return response_time * 60  # 转换为秒

# 计算 Average transaction time（平均事务处理时间）
def calculate_transaction_time(transactions, duration):
    transaction_time = duration / transactions
    return transaction_time * 60  # 转换为秒

# 根据测试使用的数据库大小（单位为 GB），计算 Scale factor
def calculate_scale_factor(db_size):
    # TPC-C 标准规模的数据库大小为 100 GB
    standard_size = 100
    scale_factor = db_size / standard_size
    return scale_factor

# 根据用户输入的测试数据，计算各种指标
def calculate_metrics():
    print("请输入以下测试数据：")
    transactions = int(input("[1]完成的事务数："))
    duration = float(input("[2]测试持续时间（单位为分钟）："))
    cost = float(input("[3]系统成本："))
    db_size = float(input("[4]测试使用的数据库大小（单位为 GB）："))

    tpm = calculate_tpm(transactions, duration)
    price_performance = calculate_price_performace(cost, tpm)
    response_time = calculate_response_time(transactions, duration)
    transaction_time = calculate_transaction_time(transactions, duration)
    scale_factor = calculate_scale_factor(db_size)

    print("\n计算结果如下：")
    print(f"Transaction throughput：{tpm:.2f} TPM（每分钟完成的事务数）")
    print(f"Price/performance ratio：${price_performance:.2f}/TPM（系统性能和成本的比率）")
    print(f"Average response time：{response_time:.2f} 秒（平均响应时间）")
    print(f"Average transaction time：{transaction_time:.2f} 秒（平均事务处理时间）")
    print(f"Scale factor：{scale_factor:.2f}（测试使用的数据库大小相对于 TPC-C 标准规模的比例）")

# 调用计算函数
calculate_metrics()
