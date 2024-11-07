
computer_hand = random.choice(hands)

if user_hand == computer_hand:
        print("引き分けです。")
    elif win_rules[user_hand] == computer_hand:
        print("あなたの勝ちです！")
        user_wins += 1
    else:
        print("コンピュータの勝ちです。")
        computer_wins += 1