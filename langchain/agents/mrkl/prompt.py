# flake8: noqa
'''
PREFIX = """Answer the following questions as best you can. You have access to the following tools:"""
FORMAT_INSTRUCTIONS = """Use the following format:

Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question"""
SUFFIX = """Begin!
'''

PREFIX = """以下の質問に答えてください。あなたは次のツールを使うことができます:"""
FORMAT_INSTRUCTIONS = """以下のフォーマットに従ってください:

質問: あなたが答えることになる質問
考え: 常に、あなたは何をすべきかを考えてください
アクション: これから行うアクション。[{tool_names}]のいずれか一つであるべきです。
アクションへの入力: アクションに対する入力
観察: アクションに対する結果
... (この、考え/アクション/アクションへの入力/観察は、N回、繰り返す可能性があります。)
考え: 私は最終回答がわかりました。
最終回答: 元の質問に対する最終的な答え"""
SUFFIX = """はじめてください!

質問: {input}
考え:{agent_scratchpad}"""
