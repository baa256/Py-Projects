from datetime import datetime , timedelta
from pytz import timezone
from colored import fg, bg, attr


Bangkok  = timezone('Asia/Bangkok')
bkk =datetime.now(Bangkok)
print ("Time in Bangkok is : " +
    bkk.strftime('%H '+ 'hour ' '%M '+ 'min ' + '%S ' + ' sec'  ))
print('\n')



ygn = bkk + timedelta(minutes= - 30 )
#ygn = timedelta(minutes=ygn.minute % 10)
print ("Time in Yangon is : " +
       ygn.strftime('%H '+ 'hour ' '%M '+ 'min ' + '%S ' + ' sec'))
print('\n')


#datetime.strptime(Bangkok, '%H:%M:%S')


#Yangon =  datetime.date(Bangkok) + dt


hawaii = timezone('US/Hawaii')
hw = datetime.now(hawaii)
print("Time in Hawaii is : " +
    hw.strftime('%H '+ 'hour ' '%M '+ 'min ' + '%S ' + ' sec'))
print('\n')

Seoul = timezone('Asia/Seoul')
Se = datetime.now(Seoul)
print("Time in Seoul is : " + 
    Se.strftime('%H '+ 'hour ' '%M '+ 'min ' + '%S ' + ' sec'))
print('\n')


Shanghai = timezone('Asia/Shanghai')
sh = datetime.now(Shanghai)
print("Time in Shanghai is : " + 
      sh.strftime('%H '+ 'hour ' '%M '+ 'min ' + '%S ' + ' sec'))
print('\n')


Tokyo = timezone('Asia/Tokyo')
ty = datetime.now(Tokyo)
print(
    "Time in Tokyo is : " +
    ty.strftime('%H '+ 'hour ' '%M '+ 'min ' + '%S ' + ' sec'))
print('\n')


Sydney = timezone('Australia/Sydney')
syd = datetime.now(Sydney)
print("Time in Sydney is : " +
      syd.strftime('%H '+ 'hour ' '%M '+ 'min ' + '%S ' + ' sec'))
print('\n')
                

London = timezone('Europe/London')
Lndn = datetime.now(London)

print( "Time in London is : " +
      Lndn.strftime('%H '+ 'hour ' '%M '+ 'min ' + '%S ' + ' sec'))


