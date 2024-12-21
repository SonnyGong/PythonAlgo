# -*- encoding: utf-8 -*-
'''
@File    :   sanlie_search.py    
@Contact :   https://github.com/SonnyGong

┌───┐ ┌───┬───┬───┬───┐ ┌───┬───┬───┬───┐ ┌───┬───┬───┬───┐ ┌───┬───┬───┐
│Esc│ │ F1│ F2│ F3│ F4│ │ F5│ F6│ F7│ F8│ │ F9│F10│F11│F12│ │P/S│S L│P/B│ ┌┐ ┌┐ ┌┐
└───┘ └───┴───┴───┴───┘ └───┴───┴───┴───┘ └───┴───┴───┴───┘ └───┴───┴───┘ └┘ └┘ └┘
┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───────┐ ┌───┬───┬───┐ ┌───┬───┬───┬───┐
│~ `│! 1│@ 2│# 3│$ 4│% 5│^ 6│& 7│* 8│( 9│) 0│_ -│+ =│ BacSp │ │Ins│Hom│PUp│ │N L│ / │ * │ - │
├───┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─────┤ ├───┼───┼───┤ ├───┼───┼───┼───┤
│ Tab │ Q │ W │ E │ R │ T │ Y │ U │ I │ O │ P │{ [│} ]│ | \ │ │Del│End│PDn│ │ 7 │ 8 │ 9 │   │
├─────┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴─────┤ └───┴───┴───┘ ├───┼───┼───┤ + │
│ Caps │ A │ S │ D │ F │ G │ H │ J │ K │ L │: ;│" '│ Enter  │               │ 4 │ 5 │ 6 │   │
├──────┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴────────┤     ┌───┐     ├───┼───┼───┼───┤
│ Shift  │ Z │ X │ C │ V │ B │ N │ M │< ,│> .│? /│ Shift    │     │ ↑ │     │ 1 │ 2 │ 3 │   │
├─────┬──┴─┬─┴──┬┴───┴───┴───┴───┴───┴──┬┴───┼───┴┬────┬────┤ ┌───┼───┼───┐ ├───┴───┼───┤ E││
│ Ctrl│WIN │Alt │ Space  @NotToday      │ Alt│ fn │ WIN│Ctrl│ │ ← │ ↓ │ → │ │ 0     │ . │←─┘│
└─────┴────┴────┴───────────────────────┴────┴────┴────┴────┘ └───┴───┴───┘ └───────┴───┴───┘

@Modify Time      @Author        @Version    @Desciption
------------      -----------    --------    -----------
2024/12/16 15:46   NotToday      1.0         None
'''


class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size
        self.load_factor = 0  # 当前载荷因子

    def hash_function(self, key):
        """简单的散列函数：计算 key 的余数"""
        return hash(key) % self.size

    def insert(self, key, value):
        """插入键值对"""
        index = self.hash_function(key)
        original_index = index
        while self.table[index] is not None:
            # 如果槽被占用但 key 相同，则更新值
            if self.table[index][0] == key:
                self.table[index] = (key, value)
                return
            # 线性探测
            index = (index + 1) % self.size
            if index == original_index:
                raise Exception("HashTable is full")
        # 插入新的键值对
        self.table[index] = (key, value)
        self.load_factor += 1 / self.size

    def search(self, key):
        """搜索键，返回对应值"""
        index = self.hash_function(key)
        original_index = index
        while self.table[index] is not None:
            if self.table[index][0] == key:  # 找到 key
                return self.table[index][1]
            index = (index + 1) % self.size
            if index == original_index:  # 已经回到起始位置，搜索失败
                break
        return None  # 搜索失败

    def delete(self, key):
        """删除键值对"""
        index = self.hash_function(key)
        original_index = index
        while self.table[index] is not None:
            if self.table[index][0] == key:
                # 找到 key 后标记为删除
                self.table[index] = None
                self.load_factor -= 1 / self.size
                return
            index = (index + 1) % self.size
            if index == original_index:
                break
        raise KeyError(f"Key {key} not found")

    def __str__(self):
        """打印散列表内容"""
        return str(self.table)


# 测试散列表
if __name__ == "__main__":
    # 创建一个散列表，大小为素数 11
    hash_table = HashTable(11)

    # 插入键值对
    hash_table.insert("apple", 100)
    hash_table.insert("banana", 200)
    hash_table.insert("cherry", 300)

    # 打印散列表
    print("HashTable:", hash_table)

    # 搜索键
    print("Search 'apple':", hash_table.search("apple"))
    print("Search 'banana':", hash_table.search("banana"))
    print("Search 'grape':", hash_table.search("grape"))  # 不存在

    # 删除键值对
    hash_table.delete("banana")
    print("HashTable after deleting 'banana':", hash_table)

    # 再次搜索已删除的键
    print("Search 'banana':", hash_table.search("banana"))
