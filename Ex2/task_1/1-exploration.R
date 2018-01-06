# --- Exploration 1 ---
> dim(iris)
> names(iris)
> str(iris)
> attributes(iris)
> iris[1:5,]
> iris[1:10, "Sepal.Length"]
> summary(iris)
> table(iris$Species)
> pie(table(iris$Species))
> var(iris$Sepal.Length)
> cov(iris$Sepal.Length, iris$Petal.Length)
> hist(iris$Sepal.Length)
>
> hist(iris$Sepal.Length, main="Sepal Length")
> plot(density(iris$Sepal.Length))
> plot(density(iris$Sepal.Length), main="Sepal Length Density")
> plot(iris$Sepal.Length, iris$Sepal.Width)
> plot(iris)
> pairs(iris)
> help(pairs)
> pairs(iris, na.action=na.omit)
> help(pairs)
> plot(iris)
> plot(iris, xlim=1)
> plot(iris, xlim=100)
> xlim off
> data(iris)
> plot(iris)

# --- Exploration 2 ---
>
> data(iris)
> iris
> class(iris)
> colnames(iris)
> iris$Petal.Length
> plot(iris$Petal.Length, iris$Petal.Width)
> plot(iris$Petal.Length, iris$Petal.Width, pch=c(23,24,25)[unclass(iris$Species)],main="Edgar Anderson's Iris Data")
> plot(iris$Petal.Length, iris$Petal.Width, pch=21 ,bg=c("red","green","blue")[unclass(iris$Species)],main="Edgar Anderson's Iris Data")
> pairs(iris[1:4],main="Edgar Anderson's Iris Data",pch=21,bg=c("red","green3","blue")[unclass(iris$Species)]
> panel.pearson <- function(x, y, ...) {
> pairs(iris[1:4], main = "Edgar Anderson's Iris Data", pch = 21, bg = c("red","green3","blue")[unclass(iris$Species)], upper.panel=panel.pearson)
> cor(iris$Sepal.Length, iris$Sepal.Width)
> cor(iris$Sepal.Length, iris$Petal.Length)
> pairs(iris[1:4], main = "Anderson's Iris Data -- 3 species", pch = 21, bg = c("red", "green3", "blue")[unclass(iris$Species)], lower.panel=NULL, labels=c("SL","SW","PL","PW"), font.labels=2, cex.labels=4.5)
> 
