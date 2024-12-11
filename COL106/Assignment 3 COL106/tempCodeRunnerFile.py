   # for m in m_values:
    #     print(f"| add_treasure() | n = 20 | m = {str(m).ljust(8)} | ", end="")
    #     test_treasury = StrawHatTreasury(m)
    #     last_added = 0
    #     for i in range(20):
    #         r = random.randint(1, 5)
    #         test_treasury.add_treasure(Treasure(i, 10 ** 9, last_added + 10 ** 9 * r))
    #         last_added += 10 ** 9 * r
    #     start_time = time.perf_counter_ns()
    #     test_treasury.add_treasure(Treasure(20, 10 ** 9, last_added + random.randint(1,5) * 10 ** 9))
    #     end_time = time.perf_counter_ns()
    #     print_str = f'{(end_time-start_time)/1000000:.4f}ms'.ljust(10)
    #     print(f'{print_str} |')
    # print("-" * 62)