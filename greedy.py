#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import List, Optional

class GreedySolution:

    def partitionLabels(self, s: str) -> List[int]:
        result = []
        if s is None or len(s) <= 0:
            return result
        
        # 找到每个字符出现的最后位置
        last = [-1] * 26
        for i in range(len(s)):
            last[ord(s[i]) - ord('a')] = i

        start, end = 0, 0
        i = 0

        for i in range(len(s)):
            # 从i出发最远能到的位置，就是第一个区间
            idx = ord(s[i]) - ord('a')
            end = max(end, last[idx])
            
            if i == end:
                result.append(end - start+1)
                start = end + 1
        
        return result


if __name__ == "__main__":
    solution = GreedySolution()
    print(solution.partitionLabels("ababcbacadefegdehijhklij"))