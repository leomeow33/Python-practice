# 权重映射字典，记录每个字符的总权重
weight_dict = {
    'A': 0, 'B': 0, 'C': 0,
    'D': 0, 'E': 0, 'F': 0,
    'G': 0, 'H': 0, 'I': 0,
    'J': 0
}
# 生成9-0依次递减的数组
nums = list(range(10))[::-1]


def make_weight(*args):
    """
    生成每个字符的权重
    :param args: 输入的字符串列表
    思路：
        1 把字符串翻转，翻转后的下标对应权重幂数
            >> ABC --> CBA
            >> 012     012
            A的权重：10^2
            B的权重：10^1
            C的权重：10^0
        2 分别计算每个字符串中，每个字符的权重，
            用字典键的唯一性作为索引
            累加每个字符的权重
    """
    for str_i in args:
        new_str = str_i[::-1]
        for i, letter in enumerate(new_str):
            weight_dict[letter] += pow(10, i)


def get_max_val():
    """
    利用权重计算最大值
    :return:
    """
    val = 0
    # 把权重按从大到小排列
    values = list(weight_dict.values())
    values.sort(reverse=True)
    #
    for i, num in enumerate(values):
        val += num * nums[i]
    return val


if __name__ == "__main__":
    # 提示用户输入
    n = input("请输入行数n: ")
    args = []
    count = 1
    while int(n) >= count:
        args.append(input("请输入第一行字符串：").upper())
        count += 1
    # 生成权重获，获取最大值
    make_weight(*args)
    result = get_max_val()
    print(weight_dict)
    print(result)