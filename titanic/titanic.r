library(randomForest)

var.in<-c( "ticket","cabin")

uczaca = read.table("train2.csv" , header=T, sep="," , colClasses=c("survived"="factor"))
uczaca <- droplevels(subset(uczaca,embarked != ""))
var.out <- setdiff(names(uczaca),var.in)
u2 <- uczaca[var.out]

for (i in 1:nrow(u2)) { 
	fare <- 1
	if(is.na(u2$fare[i])){ u2$fare[i] <- 1 }
	if( u2$fare[i] >= 30 )  { fare <- 4 }
	if( u2$fare[i] < 30 )  { fare <- 3 }
	if( u2$fare[i] < 20 )  { fare <- 2 }
	if( u2$fare[i] < 10 )  { fare <- 1 }
	u2$fare[i] <- fare	 
}
uczaca <-u2

summary(uczaca)

uczaca.na <- uczaca
set.seed(222)
uczaca <- rfImpute(survived ~ ., uczaca.na)
summary(uczaca)


testowa = read.table("test2.csv",header=T, sep=",")
testowa <- droplevels(subset(testowa,embarked != ""))

var.out<-setdiff(names(testowa),var.in)
t2  <- testowa[var.out]

for (i in 1:nrow(t2)) { 
	if(is.na(t2$age[i])){ 
		if (as.character(t2$name[i]) == "Master.") { t2$age[i] <- 4 }
		if (as.character(t2$name[i]) == "Miss.") { t2$age[i] <- 22 }
		if (as.character(t2$name[i]) == "Mr.") { t2$age[i] <- 30 }
		if (as.character(t2$name[i]) == "Mrs.") { t2$age[i] <- 38 } 
	}
	fare <- 1
	if(is.na(t2$fare[i])){ t2$fare[i] <- 1 }
	if( t2$fare[i] >= 30 )  { fare <- 4 }
	if( t2$fare[i] < 30 )  { fare <- 3 }
	if( t2$fare[i] < 20 )  { fare <- 2 }
	if( t2$fare[i] < 10 )  { fare <- 1 }
	t2$fare[i] <-fare	 	
}
testowa <-t2



set.seed(123)
las <- randomForest(survived~pclass+name+sex+age+sibsp+parch+fare+embarked,data=uczaca, ntree=5000, do.trace=25, na.action=na.fail)

importance(las)

summary(uczaca)
summary(testowa)

predict(las,testowa, type="class")


