def func():
    print("function a.py")

print("함수 밖입니다.(top-level)")

if __name__ == "__main__":
    print('직접 실행 a.py')
else:
    print("import a.py")