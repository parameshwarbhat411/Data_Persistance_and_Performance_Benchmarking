import matplotlib.pyplot as plt

def plot_query_times(times_data, query_names):
    plt.figure(figsize=(12, 8))
    for query_name in query_names:
        db_times = times_data[query_name]
        if db_times:  # Check if data is available
            plt.plot(list(db_times.keys()), list(db_times.values()), marker='o', label=query_name)

    plt.title('Query Performance Benchmark Across Databases')
    plt.xlabel('Database')
    plt.ylabel('Time (seconds)')
    plt.legend(title='Query Names',loc='upper left', bbox_to_anchor=(1, 1))
    plt.grid(True)
    plt.show()

def plot_cpu_usage(cpu_usage_data, query_names):
    plt.figure(figsize=(12, 8))
    for query_name in query_names:
        cpu_usage = cpu_usage_data[query_name]
        if cpu_usage:  # Check if data is available
            plt.plot(list(cpu_usage.keys()), list(cpu_usage.values()), marker='o', label=query_name)

    plt.title('CPU Usage During Queries Across Databases')
    plt.xlabel('Database')
    plt.ylabel('CPU Usage (%)')
    plt.legend(title='Query Names',loc='upper left', bbox_to_anchor=(1, 1))
    plt.grid(True)
    plt.show()

def plot_memory_usage(memory_usage_data, query_names):
    plt.figure(figsize=(12, 8))
    for query_name in query_names:
        memory_usage = memory_usage_data[query_name]
        if memory_usage:  # Check if data is available
            plt.plot(list(memory_usage.keys()), list(memory_usage.values()), marker='o', label=query_name)

    plt.title('Memory Usage During Queries Across Databases')
    plt.xlabel('Database')
    plt.ylabel('Memory Usage (Bytes)')
    plt.legend(title='Query Names',loc='upper left', bbox_to_anchor=(1, 1))
    plt.grid(True)
    plt.show()

# def plot_errors(error_data, query_names):
#     plt.figure(figsize=(12, 8))
#     for query_name in query_names:
#         errors = error_data[query_name]
#         if errors:  # Check if data is available
#             plt.bar(list(errors.keys()), list(errors.values()), label=query_name)
#
#     plt.title('Query Errors Across Databases')
#     plt.xlabel('Database')
#     plt.ylabel('Errors (Boolean)')
#     plt.legend(title='Query Names',loc='upper left', bbox_to_anchor=(1, 1))
#     plt.grid(True)
#     plt.show()
