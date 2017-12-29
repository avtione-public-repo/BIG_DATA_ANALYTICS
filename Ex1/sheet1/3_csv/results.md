# Python
## Result
Mean of column 1 (deltatime): 0.001295

## Execution Time
### Run 1
real    0m0.245s
user    0m0.218s
sys     0m0.023s

### Run 2
real    0m0.251s
user    0m0.223s
sys     0m0.023s

### Run 3
real    0m0.247s
user    0m0.220s
sys     0m0.023s


#R
##Result
system.time(computeMeanCSV("pitbull-ddw1024k.csv",2))
       User      System verstrichen 
       2.56        0.00        2.56 
	   
	   
system.time(computeMeanCSV("pitbull-ddw1024k.csv",2))
       User      System verstrichen 
       2.53        0.02        2.56 
	   
system.time(computeMeanCSV("pitbull-ddw1024k.csv",2))
       User      System verstrichen 
       2.55        0.00        2.58 