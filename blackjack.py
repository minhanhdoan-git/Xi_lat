import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
muon_choi = input("Chơi xì lát không? Nhấn y để chơi hoặc nhấn n để thoát: ").lower()
co_choi = True

if muon_choi == "y":
    choi_tiep = True

    while co_choi:
        your_cards = list()
        your_current_score = 0
        your_cards += random.choices(cards,k = 2)
        for i in your_cards:
            your_current_score += i

        computer_cards = list()
        computer_current_score = 0
        computer_cards += random.choices(cards,k = 2)
        for i in computer_cards:
            computer_current_score += i

        print(f"Bài của bạn:{your_cards}, tổng điểm hiện tại của bạn là: {your_current_score}")
        print(f"Lá bài đầu tiên của máy: {computer_cards[0]}")

        while choi_tiep:
            tiep = input("Nhấn y để nhận thêm lá bài mới, nhấn n để bỏ qua: ")
            if tiep == "y":
                your_new_card = random.choice(cards)
                your_cards.append(your_new_card)
                your_current_score += your_new_card
                print(f"Bài của bạn:{your_cards}, tổng điểm hiện tại của bạn là: {your_current_score}")
                if your_current_score <= 21:
                    print(f"Lá bài đầu tiên của máy: {computer_cards[0]}")

                elif your_current_score > 21:
                    if 11 in your_cards:
                        for i in range(len(your_cards)):
                            if your_cards[i] == 11:
                                your_cards[i] = 1
                                print(f"Bài của bạn:{your_cards}, tổng điểm hiện tại của bạn là: {your_current_score}")
                                print(f"Lá bài đầu tiên của máy: {computer_cards[0]}")

                    else:
                        
                        print("Quá 21 điểm, bạn đã thua!")
                        choi_tiep = False

            else:
                choi_tiep = False
                while computer_current_score < 17:
                    computer_new_card = random.choice(cards)
                    computer_cards.append(computer_new_card)
                    computer_current_score += computer_new_card
                if computer_current_score < your_current_score:
                    print(f"Bài của máy tính: {computer_cards}, bài của bạn: {your_cards}")
                    print("Bạn thắng rồi!")
                elif computer_current_score == your_current_score:
                    print(f"Bài của máy tính: {computer_cards}, bài của bạn: {your_cards}")
                    print("Hòa!")
                else:
                    print(f"Bài của máy tính: {computer_cards}, bài của bạn: {your_cards}")
                    print("Bạn thua rồi!")

else:
    co_choi = False