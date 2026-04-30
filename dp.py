#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import List, Optional

class DpSolution:

    def longestValidParentheses(self, s: str) -> int:
        if s is None or len(s) <= 1:
            return 0
        
        stack = []
        result = 0

        # 栈里放当前没配对的
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else: # 右括号
                if len(stack) > 0 and s[stack[-1]] == '(':
                    stack.pop() # 已配对，出栈
                    # 更新最大长度
                    if len(stack) > 0:
                        # 栈里面是没配对的最远位置
                        result = max(result, i - stack[-1])
                    else:
                        result = max(result, i + 1)
                else:
                    stack.append(i)
        
        return result
    

if __name__ == "__main__":
    dp = DpSolution()
    print(dp.longestValidParentheses("(()"))