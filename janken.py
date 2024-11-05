
# ジャンケンの手を定義
hands = ["グー", "チョキ", "パー"]
# 勝敗を判定するためのルール
win_rules = {
    "グー": "チョキ",
    "チョキ": "パー",
    "パー": "グー"
}
# 対戦回数
rounds = 3
# 各ラウンドの結果を記録
user_wins = 0
computer_wins = 0
print("ジャンケンゲームを開始します。")
for i in range(rounds):
    print(f"\nラウンド {i + 1}")
    print("1: グー, 2: チョキ, 3: パー")
    # ユーザの入力を取得

    # 入力が正しいか確認
    while user_input not in ["1", "2", "3"]:
        user_input = input("無効な入力です。1, 2, 3のいずれかを選んでください: ")

    # 勝敗を判定

# 最終結果を表示
print("\nゲーム終了")
print(f"あなたの勝ち: {user_wins}回")
print(f"コンピュータの勝ち: {computer_wins}回")
if user_wins > computer_wins:
    print("最終結果: あなたの勝ちです！")
elif user_wins < computer_wins:
    print("最終結果: コンピュータの勝ちです。")
else:
    print("最終結果: 引き分けです。")