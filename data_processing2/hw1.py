# 인스타그램 흉내내기
class User:
    def __init__(self, name, email, password, auto = True):
        self.name = name
        self.email = email
        self.__password = password
        self.__following_list = []    # 본인이 팔로우하는 유저 리스트
        self.__followers_list = []    # 본인을 팔로우하는 유저 리스트
        self.__auto_accept = auto     # 자동으로 팔로우 요청 수락할건지
        self.__request_follow = []    # 본인에게 팔로우 요청, 대기 유저 리스트

    def __str__(self):                # 유저 객체를 이름으로
        return self.name

    # 팔로우
    def follow(self, another_user):
        accepted = another_user.append_follower(self)   # 상대방에게 팔로우 요청 보냄
        if accepted:        # 상대방의 auto_accept 여부 받음
            self.__following_list.append(another_user)  # 자동 수락이면 본인의 팔로잉 리스트에 추가

    # 상대방에게 팔로우 요청하기
    def append_follower(self, request_user):        # request_user => 팔로우 요청한 유저
        if self.__auto_accept:
            self.__followers_list.append(request_user)      # 상대방이 자동 수락이면 상대방의 팔로워 리스트에 request_user 추가
            print("To",self, "-", request_user, "님이", self, "(을)를 팔로우합니다.")
            return True                             # 자동 수락 정보 리턴
        else:
            self.__request_follow.append(request_user)      # 상대방이 자동 수락아니면 상대방의 팔로우 요청 대기 명단에 추가
            print("To",self, "-", request_user, "님이", self, "(을)를 팔로우 신청했습니다.")
            return False                            # 자동 수락 x 정보 리턴

    # 나에게 들어온 팔로우 요청 리스트 체크
    def check_request(self):
        while len(self.__request_follow) > 0:       # 대기 리스트가 빌 때 까지
            user = self.__request_follow.pop(-1)
            print("To",self, "-", user.name, end=" ")
            answer = input("님의 팔로우 요청을 수락하시겠습니까? (y/n)")
            if answer == "y" or answer == "Y":
                self.__followers_list.append(user)  # 수락하면 리스트에 추가
                accept = True                       # 수락했다는 정보 리턴
                print("To",self, "-", user,"님의 팔로우 요청을 수락하셨습니다.")
                print()
            else:
                accept = False                      # 거절했다는 정보 리턴
                print("To",self, "-", user,"님의 팔로우 요청을 거절하셨습니다.")
                print()

            user.accept_follow(self, accept)        # 수락/거절 정보를 해당 유저에게 보냄
        return

    # 상대방에게 보낸 팔로우 요청 수락/거절 여부 확인
    def accept_follow(self, accept_user, accept):
        if accept:
            self.__following_list.append(accept_user)   # 수락 값이 넘어왔으면 나의 팔로잉 리스트에 추가
            print("To",self, "-", accept_user,"님이", self, "님의 팔로우 요청을 수락하셨습니다.\n")

        else:
            print("To",self, "-", accept_user, "님이 팔로우 요청을 거절하셨습니다.\n")

    # auto_accept 값 변경 함수
    def setAutoaccept(self, check):
        if check == True:
            self.__auto_accept = True
        else:
            self.__auto_accept = False

    # 팔로잉 리스트 리턴
    def getFollowing(self):
        return [i.name for i in self.__following_list]
    # 팔로워 리스트 리턴
    def getFollower(self):
        return [i.name for i in self.__followers_list]

    # 몇명을 팔로우하는지 리턴
    def getNum_following(self):
        return len(self.__following_list)

    # 팔로워가 몇명인지 리턴
    def getNum_followers(self):
        return len(self.__followers_list)

    # 비밀번호 변경하기
    def change_password(self):
        while True:
            pw = input("현재 비밀번호를 입력하세요 : ")
            if pw == self.__password:
                new_pw = input("새로운 비밀번호를 입력하세요 : ")
                self.__password =  new_pw
                print("변경 완료")
                break
            else:
                print("틀렸습니다. 다시 입력해주세요")

    # 유저 정보 리턴
    def __call__(self):
        return print("이름 : " + self.name, "이메일 : " + self.email, "팔로잉 : " + str(self.getNum_following()), "팔로워 : " + str(self.getNum_followers()))

user1 = User("kjh", "kjh@naver.com", "123456")
user2 = User("abc", "abc@naver.com", "abcdef", False)
user3 = User("def", "def@naver.com", "123abc")
user4 = User("ghi", "ghi@naver.com", "abc123")

# 테스트
# 비밀번호 변경
user1.change_password()

#팔로우 하기
print()
user1.follow(user3)
print()
user2.follow(user1)
print()
user2.follow(user3)
print()
user2.follow(user4)
print()
user4.follow(user2)
print()
user1.follow(user2)
print()

# 자동 수락 아닌 유저의 요청 리스트 확인
user2.check_request()
print()

# 각 유저의 팔로워 리스트 확인
print(user1,"님의 팔로워", user1.getFollower())
print(user2,"님의 팔로워", user2.getFollower())
print(user3,"님의 팔로워", user3.getFollower())
print(user4,"님의 팔로워", user4.getFollower())

# 유저 정보 확인
print()
user1()
user2()
user3()
user4()