'''
- 객체의 종류는 제약 없음 (학생 객체, 선생 객체, 계좌 객체 등)
- 객체의 속성을 최소 5가지 이상 정의
- 객체의 메소드를 최소 5가지 이상 정의
- 테스트 코드 추가
'''

#팔로워
class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.__password = password
        self.following_list = []    # 본인이 팔로우하는 유저 리스트
        self.followers_list = []    # 본인을 팔로우하는 유저 리스트

    # 팔로우
    def follow(self, another_user):
        self.following_list.append(another_user)
        another_user.followers_list.append(self)
        print(self.name,"(이)가",another_user.name,"(을)를 팔로우합니다.")

    # 몇명을 팔로우하는지 리턴
    def num_following(self):
        return len(self.following_list)

    # 팔로워가 몇명인지 리턴
    def num_followers(self):
        return len(self.followers_list)

    def change_password(self):
        while True:
            pw = input("현재 비밀번호를 입력하세요")
            if pw == self.__password:
                new_pw = input("새로운 비밀번호를 입력하세요")
                self.__password =  new_pw
                print("변경 완료")
                break
            else:
                print("틀렸습니다. 다시 입력해주세요")

    def check_pw(self, email):
            if email == self.email:
                return (self.__password)
            else:
                return ("틀렸습니다.")

    def get_info(self):
        return ("이름 : " + self.name, "이메일 : " + self.email, "팔로잉 : " + str(self.num_following()), "팔로워 : " + str(self.num_followers()))

user1 = User("kjh", "kjh@naver.com", "123456")
user2 = User("abc", "abc@naver.com", "abcdef")
user3 = User("def", "def@naver.com", "123abc")
user4 = User("ghi", "ghi@naver.com", "abc123")

# 테스트
user1.change_password()
print("비밀번호", user1.check_pw("kjh@naver.com"))
print()
user1.follow(user2)
user1.follow(user3)
user2.follow(user1)
user2.follow(user3)
user2.follow(user4)
user4.follow(user1)
print()
print(user1.get_info())
print(user2.get_info())
print(user3.get_info())
print(user4.get_info())
