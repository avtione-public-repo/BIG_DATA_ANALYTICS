summary = summaryCodings()
summary
table = getCodingTable()
table

codings = table$codename
codings

f_codings = factor(codings)
f_codings
l_codings = levels(f_codings)
l_codings

s_codings <- sample(table$codename, 100, replace=TRUE)

# Add extra space to right of plot area; change clipping to figure
#par(mar=c(5.1, 4.1, 4.1, 8.1), xpd=TRUE)

barplot(summary$NumOfCoding, xlab="Data Codings", ylab="Frequency", main="Total of Coding Numbers", cex.lab=1, beside = T, col = rainbow(15))

#barplot(table(s_codings), beside = T,
#        col = 1:15, space = c(0, 2))

legend("topright", 
       legend = l_codings, 
       fill = rainbow(15), ncol = 2,
       cex = 0.75)

#barplot(summary$AvgLength, main="Summary of Coding Number per File", beside = T, col = rainbow(15))
barplot(summary$AvgLength, xlab="Data Codings", ylab="Frequency", main="Coding Length Average", cex.lab=1, beside = T, col = rainbow(15))
legend("topright", 
       legend = l_codings, 
       fill = rainbow(15), ncol = 2,
       cex = 0.75)

barplot(summary$NumOfFile, xlab="Data Codings", ylab="Frequency", main="Coding per Article", cex.lab=1, beside = T, col = rainbow(15))
#legend("topright", 
#       inset=c(-0.2,0),
#       legend = l_codings, 
#       fill = rainbow(15), ncol = 2,
#       cex = 0.75)

