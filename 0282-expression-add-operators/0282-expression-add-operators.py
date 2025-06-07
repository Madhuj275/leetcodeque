class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        possible_expressions = []
        n = len(num)

        def backtrack(
            position: int,
            expression_parts: list,
            expression_result: int,
            previous_operand: int
        ):
            if position == n:
                if expression_result == target:
                    possible_expressions.append(''.join(expression_parts))
                return

            current_operand = 0
            for i in range(position, n):
                if num[position] == '0' and i > position:
                    return
                    
                current_operand = current_operand * 10 + int(num[i])
                
                if position == 0:
                    expression_parts.append(str(current_operand))
                    backtrack(i + 1, expression_parts, current_operand, current_operand)
                    expression_parts.pop()
                else:
                    for operator in '*+-':
                        expression_parts.extend([operator, str(current_operand)])
                        
                        if operator == '+':
                            backtrack(
                                i + 1, expression_parts, 
                                expression_result + current_operand, current_operand
                            )
                        elif operator == '-':
                            backtrack(
                                i + 1, expression_parts, 
                                expression_result - current_operand,-current_operand
                            )
                        else:
                            backtrack(
                                i + 1,
                                expression_parts,
                                expression_result - previous_operand + 
                                (current_operand * previous_operand),
                                current_operand * previous_operand
                            )
                        
                        expression_parts.pop() 
                        expression_parts.pop() 

        backtrack(0, [], 0, 0)
        return possible_expressions
 
        