
```
{
  "task": "파이썬 함수 구현",
  "goal": "두 개의 숫자 리스트에 대해 사칙연산(덧셈, 뺄셈, 곱셈, 나눗셈)을 모두 수행하고 결과를 반환하는 함수를 구현하고, 제공된 테스트 리스트를 사용해 해당 함수를 실행하는 전체 코드를 작성하시오.",
  "constraints": {
    "data_type": "테스트 데이터는 리스트(list)로만 제공되어야 함.",
    "test_data_count": "테스트 데이터 쌍은 10개여야 함.",
    "variable_naming": "변수명은 소문자와 언더스코어(_) 조합을 사용해야 함.",
    "function_signature": "함수는 두 개의 숫자(a, b)를 입력받아야 함.",
    "function_output": "함수는 덧셈, 뺄셈, 곱셈, 나눗셈 결과를 모두 포함하는 튜플 또는 리스트 형태로 반환해야 함.",
    "division_by_zero_handling": "나눗셈에서 0으로 나누는 경우, 해당 나눗셈 결과 대신 문자열 \"division_error\"를 반환해야 함."
  },
  "structure": {
    "test_data_definition": [
      {
        "variable_name": "test_a",
        "values": [10, 25, 40, 12, 7, 9, 16, 100, 3, 81]
      },
      {
        "variable_name": "test_b",
        "values": [5, 5, 8, 3, 0, 3, 2, 4, 9, 9]
      }
    ],
    "function_definition": {
      "name": "perform_arithmetic_operations",
      "parameters": ["num_a", "num_b"],
      "logic": "덧셈, 뺄셈, 곱셈을 계산하고, 나눗셈은 num_b가 0인지 확인하여 처리해야 함. 모든 결과를 순서대로 묶어 반환해야 함."
    },
    "execution_block": {
      "loop": "range(10)을 사용하여 test_a와 test_b의 요소를 반복 접근",
      "call": "반복문 내에서 정의된 함수 호출",
      "output": "print(f\"{a}, {b} => {result}\") 형식으로 출력"
    }
  },
  "implementation_language": "Python",
  "file_name": "prompts/01_functions.py"
}
```