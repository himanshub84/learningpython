magic_number=7
count_num=0
limit_count=3
while count_num < limit_count :
    guss_no=int(input('Guss the Number'))
    count_num += 1
    if magic_number==guss_no :
        print('wolaa you have guss the right number')
        break
else :
    print('you are failed ')
