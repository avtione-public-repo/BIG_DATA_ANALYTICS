args = commandArgs(trailingOnly = TRUE)
computeMeanCSV = function(dateiname, spaltenNr){
  
  conn <- file(dateiname,open="r")
  linn <-readLines(conn)
  output = rep(2:length(linn))
  for (i in 2:length(linn)){
    lineElement = strsplit(linn[i],",")[[1]][2]
    output[i-2] <- lineElement
  } 
  close(conn)
  computeMeanCSV = output
}
system.time(computeMeanCSV("pitbull-ddw1024k.csv",2))


