import a #a.py를 import
import test
print("top-level : b.py")

a.func()
if __name__ == "__main__":
    print('b.py를 직접 실행')
else:
    print("b.py를 import 시켜서 실행")