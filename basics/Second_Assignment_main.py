from Second_Assignmet import WriteFile,CSVFormatter,LogFormatter

writecsv=WriteFile('text2.csv',CSVFormatter)
writelog=WriteFile('log.txt',LogFormatter)

writecsv.write(['a','b.2','c','d'])
writelog.write('this is log message')

writecsv.write(['1','2','3','4'])
writelog.write(['this is another log message'])
writecsv.close()
writelog.close()