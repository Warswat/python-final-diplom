from tasks import add

def main():
    async_result1 = add.delay(1, 2)
    async_result2 = add.delay(1, 4)
    async_result3 = add.delay(5, 4)
    async_result4 = add.delay(2, 4)
    print(async_result1.get())

main()
print("end")